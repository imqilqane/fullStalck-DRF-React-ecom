from django.shortcuts import render
from config.utils import get_buyer
from rest_framework import generics, serializers, status
from .serializers import AddAdressSerializer, PaymentSerializer
from User.models import User
from rest_framework.response import Response
from Products.models import Order, OrderdItem
from .models import Address, Payment
import stripe
import string
import random


stripe.api_key = "sk_test_1srueIi8nRsob787g1O3pS0z00NR4rSjbb"


class AddAdressAPIView(generics.GenericAPIView):
    serializer_class = AddAdressSerializer

    def post(self, request):
        user = get_buyer(request)
        order_qs = Order.objects.filter(buyer=user, in_processing=False)

        if order_qs.exists():
            order = order_qs[0]

            if request.data['use_default']:
                address_qs = Address.objects.filter(
                    buyer=user, is_default=True)
                if address_qs.exists():
                    address = address_qs[0]
                    order.address = address
                    order.save()
                    return Response({'success:': 'user using the default adress'}, status=status.HTTP_200_OK)

                else:
                    return Response({'error:': 'user has no default address'}, status=status.HTTP_400_BAD_REQUEST)

            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            address = serializer.save()
            address.buyer = user
            address.save()

            if request.data['is_default']:
                try:
                    prevouis_default = Address.objects.get(
                        buyer=user, is_default=True)
                    prevouis_default.is_default = False
                    prevouis_default.save()
                except:
                    pass
                address.is_default = True
                address.save()

            order.address = address
            order.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


def GenOrderNum():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))


class PaymentAPIView(generics.GenericAPIView):
    serializer_class = PaymentSerializer

    def post(self, request):
        user = get_buyer(request)
        token = request.data['public_key']
        payment_method_id = request.data['payment_method_id']

        try:
            order = Order.objects.get(buyer=user, in_processing=False)
            amount = int(order.get_order_total() * 100)
            try:
                # check if this customer is aleaready exists in stripe
                customer_data = stripe.Customer.list(
                    email=user.email).data
                if len(customer_data) == 0:
                    # its mean that the customer is not exists
                    # creat customer btw the email should be passed from the front end as well ot get it from the acess token as i did now
                    customer = stripe.Customer.create(
                        email=user.email,
                        payment_method=payment_method_id
                    )
                else:
                    # get the customer
                    customer = customer_data[0]
                    extra_msg = "Customer already existed."
                # lets charg the custumer rn
                charge = stripe.PaymentIntent.create(
                    customer=customer,
                    payment_method=payment_method_id,
                    currency='usd',
                    amount=amount,
                    confirm=True
                )
                payment = Payment(
                    stripe_charge_id=charge['id'],
                    amount=order.get_order_total()
                )

                payment.save()

                ordered_items = order.products.all()
                for item in ordered_items:
                    item.ordered = True
                    item.save()

                order.payment = payment
                order.number = GenOrderNum()
                order.in_processing = True
                order.save()
                return Response({'success:': 'payment went great'}, status=status.HTTP_200_OK)
            except stripe.error.CardError as e:
                # Since it's a decline, stripe.error.CardError will be caught
                print('Status is: %s' % e.http_status)
                print('Type is: %s' % e.error.type)
                print('Code is: %s' % e.error.code)
                # param is '' in this case
                print('Param is: %s' % e.error.param)
                print('Message is: %s' % e.error.message)
                return Response({'error:': 'try again later'}, status=status.HTTP_400_BAD_REQUEST)

            except stripe.error.RateLimitError as e:
                # Too many requests made to the API too quickly
                return Response({'error:': 'Rate limit error'}, status=status.HTTP_400_BAD_REQUEST)

            except stripe.error.InvalidRequestError as e:
                # Invalid parameters were supplied to Stripe's API
                return Response({'error:': 'invalid paramiters'}, status=status.HTTP_400_BAD_REQUEST)

            except stripe.error.AuthenticationError as e:
                # Authentication with Stripe's API failed
                # (maybe you changed API keys recently)
                return Response({'error:': 'not authenticated'}, status=status.HTTP_400_BAD_REQUEST)

            except stripe.error.APIConnectionError as e:
                # Network communication with Stripe failed
                return Response({'error:': 'network error'}, status=status.HTTP_400_BAD_REQUEST)

            except stripe.error.StripeError as e:
                # Display a very generic error to the user, and maybe send
                # yourself an email
                return Response({'error:': 'something wents worng you will not charged please try again'}, status=status.HTTP_400_BAD_REQUEST)

            except Exception as e:
                # send email to ouselves
                return Response({'error:': 'there is some thing to fix in our website you will not charged please try again later'}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({'error:': 'No such order'}, status=status.HTTP_400_BAD_REQUEST)
