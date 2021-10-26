from django.core import exceptions
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Address


class AddAdressSerializer(serializers.ModelSerializer):
    is_default = serializers.BooleanField()

    class Meta:
        model = Address
        fields = [
            "buyer",
            "street",
            "zip_code",
            "city",
            "country",
            "is_default",
        ]

    def validate(self, attrs):
        print("attrs => ", attrs)
        data = {
            "street": attrs.get('street'),
            "zip_code": attrs.get('zip_code'),
            "city": attrs.get('city'),
            "country": attrs.get('country'),
            "is_default": attrs.get('is_default'),
        }
        return data

    def create(self, validate_data):
        print("validate_data => ", validate_data)
        address = Address.objects.create(**validate_data)
        return address


class PaymentSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=225)

    class Meta:
        fields = ['token', ]
