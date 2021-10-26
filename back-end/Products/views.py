from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework import response, permissions, generics, exceptions
from .serializers import *
from .models import *
from rest_framework.response import Response
# from rest_framework import pres
from rest_framework import status
from config.utils import get_buyer


class ListProductsAPIView(generics.ListAPIView):
    # premissions_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CatsListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer


class SingleProductAPIView(generics.GenericAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):

        pk = self.kwargs.get('pk')
        try:
            product = Product.objects.get(slug=pk)
        except:
            product = Product.objects.get(id=pk)

        return product

    def get(self, request,  pk):
        serializer = self.serializer_class(self.get_queryset())
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryProductsAPIView(generics.GenericAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_name = self.kwargs.get('pk')
        category = Category.objects.get(name=category_name)
        products = Product.objects.filter(category=category)
        return products

    def get(self, request, pk):
        serializer = self.serializer_class(
            self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddToCartAPIView(generics.GenericAPIView):

    def get(self, request, pk):
        user = get_buyer(request)
        print(user)
        product = get_object_or_404(Product, id=pk)
        ordered_product_qs = OrderdItem.objects.filter(
            product=product, ordered=False)
        if ordered_product_qs.exists():
            ordered_product = ordered_product_qs[0]
            ordered_product.quantity += 1
            ordered_product.save()
            return Response({'success': 'item quantity updated'}, status=status.HTTP_200_OK)
        else:
            order_qs = Order.objects.filter(buyer=user, in_processing=False)
            ordered_product = OrderdItem.objects.create(
                buyer=user, product=product)

            if order_qs.exists():
                order = order_qs[0]
                order.products.add(ordered_product)
                order.save()
                return Response({'success': 'item added to your cart'}, status=status.HTTP_200_OK)

            else:
                order = Order.objects.create(buyer=user)
                order.products.add(ordered_product)
                order.save()
                return Response({'success': 'item added to your cart'}, status=status.HTTP_200_OK)


class DecreaseQtAPIView(generics.GenericAPIView):

    def get(self, request, pk):
        user = get_buyer(request)
        product = get_object_or_404(Product, id=pk)
        ordered_product_qs = OrderdItem.objects.filter(
            product=product, ordered=False)
        if ordered_product_qs.exists():
            ordered_product = ordered_product_qs[0]
            if ordered_product.quantity > 1:
                ordered_product.quantity -= 1
                ordered_product.save()
                return Response({'success': 'item quantity updated'}, status=status.HTTP_200_OK)
            else:
                order_qs = Order.objects.filter(
                    buyer=user, in_processing=False)
                if order_qs.exists():
                    order = order_qs[0]
                    if len(order.products.all()) == 1:
                        order.delete()
                    else:
                        order.remove(ordered_product)
                        order.save()

                ordered_product.delete()

                return Response({'success': 'item has removed from your cart'}, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'No such item'}, status=status.HTTP_400_BAD_REQUEST)


class RemoveFromCartAPIView(generics.GenericAPIView):

    def get(self, request, pk):
        user = get_buyer(request)
        product = get_object_or_404(Product, id=pk)
        ordered_product_qs = OrderdItem.objects.filter(
            product=product, ordered=False)
        if ordered_product_qs.exists():
            ordered_product = ordered_product_qs[0]
            order_qs = Order.objects.filter(buyer=user, in_processing=False)
            if order_qs.exists():
                order = order_qs[0]
                if len(order.products.all()) == 1:
                    order.delete()
                else:
                    order.remove(ordered_product)
                    order.save()
            ordered_product.delete()
            return Response({'success': 'item has removed from your cart'}, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'No such item'}, status=status.HTTP_400_BAD_REQUEST)


class CartAPIView(generics.GenericAPIView):
    serializer_class = CartSerializer

    def get_queryset(self, request):
        user = get_buyer(request)
        cart = OrderdItem.objects.filter(buyer=user, ordered=False)
        return cart

    def get(self, request):
        serializer = self.serializer_class(
            self.get_queryset(request), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
