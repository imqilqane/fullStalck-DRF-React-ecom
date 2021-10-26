from typing import Counter
from django.db import models
from User.models import User
# Create your models here.


class Address(models.Model):
    buyer = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    street = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    is_default = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.buyer.username} => {self.street}"


class Payment(models.Model):
    buyer = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    stripe_charge_id = models.CharField(max_length=100)
    amount = models.FloatField()

    def __str__(self):
        return self.stripe_charge_id
