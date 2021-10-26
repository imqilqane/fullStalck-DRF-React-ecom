from django.contrib import admin
from .models import Address, Payment


class AddressManager(admin.ModelAdmin):
    list_display = [
        "buyer",
        "street",
        "zip_code",
        "city",
        "country",
        "is_default",
    ]


admin.site.register(Address, AddressManager)
admin.site.register(Payment)
