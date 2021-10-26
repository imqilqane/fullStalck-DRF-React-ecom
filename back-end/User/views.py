from django.shortcuts import render
from django.urls import reverse
from .serializers import (
    UserRegesterationSerializer,
    LoginSerializer,
    RequestPasswordResetSerializer,
    PasswordResetSerializer,
    LogoutSerializer
)
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import generics, serializers
from django.core.mail import EmailMessage
from rest_framework.response import Response
from rest_framework import status
import jwt
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import DjangoUnicodeDecodeError, smart_bytes, smart_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import permissions


class UserRegister(generics.GenericAPIView):
    serializer_class = UserRegesterationSerializer
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = User.objects.get(email=serializer.data['email'])
        token = RefreshToken.for_user(user).access_token
        main_link = get_current_site(request).domain
        relative_link = reverse('User:verifing')
        absolute_link = f"http://localhost:3000{relative_link}?token={token}"

        obj = "Verify your account"
        body = f"""hello dear {user.username} \n we are glad to have you in our webiser, you still
        have one step to go by verfing your account trough this link \n 
        {absolute_link}
        """
        email = EmailMessage(
            obj,
            body,
            'no-replay@hoom.com',
            [user.email, ]
        )
        email.send()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserAccountVerification(generics.GenericAPIView):
    def get(self, request):
        try:
            token = request.GET.get('token')
            playload = jwt.decode(
                jwt=token, key=settings.SECRET_KEY, algorithms=["HS256"])
            user_id = playload['user_id']
            user_qs = User.objects.filter(id=user_id)
            if user_qs.exists():
                user = user_qs[0]
                user.is_verified = True
                user.save()
                return Response({'success': 'account verified'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({'Error': 'Token is expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response({'Error': 'Token is invalid'}, status=status.HTTP_400_BAD_REQUEST)


class LoginUserView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestPasswordResetView(generics.GenericAPIView):
    serializer_class = RequestPasswordResetSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_qs = User.objects.filter(email=serializer.data['email'])
        if user_qs.exists():
            user = user_qs[0]
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)

            host = get_current_site(request).domain
            relative_link = reverse('user:reset', kwargs={
                                    'uidb64': uidb64, 'token': token})
            absolute_link = f'http://{host}{relative_link}'

            obj = "Verify your account"
            body = f"""hello dear {user.username} \n we are glad to have you in our webiser, you to reset your password click on this link \n 
            {absolute_link}
            """
            email = EmailMessage(
                obj,
                body,
                'no-replay@hoom.com',
                [user.email, ]
            )
            email.send()

            return Response(serializer.data, status=status.HTTP_200_OK)


class ResetPasswordView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer

    def patch(self, request, uidb64, token):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'password has sucessfuly reset'}, status=status.HTTP_200_OK)


class LogOutView(generics.GenericAPIView):

    serializer_class = LogoutSerializer
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        # try:
        refresh_token = request.data.get('refresh_token')
        print(refresh_token)
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({'success': 'Loged Out'}, status=status.HTTP_200_OK)
        # except:
        #     return Response({'Error': 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
