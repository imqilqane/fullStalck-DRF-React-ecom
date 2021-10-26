from django.db import models
from django.template.defaultfilters import default, slugify
from checkout.models import Address, Payment
from User.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):

    def get_image_path(inctance, filename):
        return f'product_pics/{inctance.category.slug}/{inctance.title}/{filename}'

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True, max_length=500)
    price = models.FloatField()
    main_image = models.ImageField(upload_to=get_image_path, max_length=500)
    image_2 = models.ImageField(
        upload_to=get_image_path, null=True, blank=True, max_length=500)
    image_3 = models.ImageField(
        upload_to=get_image_path, null=True, blank=True, max_length=500)
    image_4 = models.ImageField(
        upload_to=get_image_path, null=True, blank=True, max_length=500)
    image_5 = models.ImageField(
        upload_to=get_image_path, null=True, blank=True, max_length=500)
    image_6 = models.ImageField(
        upload_to=get_image_path, null=True, blank=True, max_length=500)
    image_7 = models.ImageField(
        upload_to=get_image_path, null=True, blank=True, max_length=500)
    image_8 = models.ImageField(
        upload_to=get_image_path, null=True, blank=True, max_length=500)
    stock = models.IntegerField(default=1)
    description = models.TextField()
    published = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-published', ]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class OrderdItem(models.Model):
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_in = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    ordered = models.BooleanField(default=False)

    class Meta:
        ordering = ['-added_in', ]

    def get_product_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.quantity} X {self.product.title}'


class Order(models.Model):
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1)
    products = models.ManyToManyField(OrderdItem)
    added_in = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    in_processing = models.BooleanField(default=False)
    address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, blank=True)
    number = models.CharField(max_length=25)
    payment = models.ForeignKey(
        Payment, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-added_in', ]

    def __str__(self):
        return self.buyer.username

    def get_order_total(self):
        total = 0
        for product in self.products.all():
            total += product.get_product_total()
        return total
