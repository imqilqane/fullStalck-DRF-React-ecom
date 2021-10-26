from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework import exceptions
from django.contrib.auth import authenticate
from .models import User
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str


class UserRegesterationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=25, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            'password'
        ]

    def validate(self, attrs):
        username = attrs.get('username')

        if not username.isalnum():
            raise exceptions.ValidationError(
                'username must contains letters as well')

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(
        max_length=25, write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['email', 'password', 'token']

    def get_token(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access'],
        }

    def validate(self, attrs):

        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = authenticate(email=email, password=password)

        if not user:
            raise exceptions.AuthenticationFailed('there is no such user')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('Your account is blocked')

        if not user.is_verified:
            raise exceptions.AuthenticationFailed(
                'Your account is not verfied yet')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens()
        }


class RequestPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ['email', ]


class PasswordResetSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=25, write_only=True)
    uidb64 = serializers.CharField(max_length=255)

    class Meta:
        fields = ["token",
                  "password",
                  "uidb64",
                  ]

    def validate(self, attrs):
        token = attrs.get('token')
        password = attrs.get('password')
        uidb64 = attrs.get('uidb64')

        id = smart_str(urlsafe_base64_decode(uidb64))
        user_qs = User.objects.filter(id=id)
        if user_qs.exists():
            user = user_qs[0]
            token = PasswordResetTokenGenerator().check_token(user, token)
            if not token:
                raise exceptions.ValidationError('token is in valid')

            user.set_password(password)
            user.save()
            return super().validate(attrs)

        else:
            raise exceptions.ValidationError('user is not exists')


class LogoutSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=500)

    class Meta:
        fields = ['token', ]
