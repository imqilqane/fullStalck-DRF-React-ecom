# Generated by Django 3.2.8 on 2021-10-09 12:10

import Products.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_auto_20211009_1238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=Products.models.Product.get_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_3',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=Products.models.Product.get_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_4',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=Products.models.Product.get_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_5',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=Products.models.Product.get_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_6',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=Products.models.Product.get_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_7',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=Products.models.Product.get_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_8',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=Products.models.Product.get_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.ImageField(max_length=500, upload_to=Products.models.Product.get_image_path),
        ),
    ]