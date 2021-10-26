from django.contrib import admin

from .models import Product, Category, OrderdItem, Order


class ProductsManager(admin.ModelAdmin):

    list_display = [
        "title",
        "category",
        "price",
        'stock'
    ]


class OrderdItemManager(admin.ModelAdmin):

    list_display = [
        "buyer",
        "product",
        "quantity",
        'added_in',
        "ordered"

    ]


class OrderManager(admin.ModelAdmin):

    list_display = [
        "buyer",
        "added_in",
        'in_processing',
        'number',
        'payment'


    ]


admin.site.register(Product, ProductsManager)
admin.site.register(Category)
admin.site.register(OrderdItem, OrderdItemManager)
admin.site.register(Order, OrderManager)
