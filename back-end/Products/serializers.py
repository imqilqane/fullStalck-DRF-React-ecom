from django.db.models import fields
from . import models
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderdItem
        fields = '__all__'


class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id', ]
