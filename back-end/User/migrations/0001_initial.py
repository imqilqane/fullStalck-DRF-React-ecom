# Generated by Django 3.2.8 on 2021-10-07 13:42

import User.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('picture', models.ImageField(default='user_pics/dafault.png', upload_to=User.models.User.get_user_pic_path)),
                ('last_login', models.DateTimeField()),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', User.models.UserManager()),
            ],
        ),
    ]
