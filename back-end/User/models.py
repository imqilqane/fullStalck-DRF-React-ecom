from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from rest_framework_simplejwt import tokens


class UserManager(UserManager):

    def create_user(self, username, email, password, first_name=None, last_name=None):
        if not username:
            raise ValueError('user has to have a username')

        if not email:
            raise ValueError('user has to have an email')

        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    def get_user_pic_path(self):
        return f'user_pics/{self.username}/'

    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(
        verbose_name="email address", max_length=255, unique=True)
    first_name = models.CharField(max_length=20,)
    last_name = models.CharField(max_length=20,)
    picture = models.ImageField(
        upload_to=get_user_pic_path, default='user_pics/dafault.png')
    last_logind = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.username

    def has_prem(self, prem, obj=None):
        return self.is_admin

    def tokens(self):
        return {
            'refresh': str(tokens.RefreshToken.for_user(self)),
            'access': str(tokens.RefreshToken.for_user(self).access_token)
        }
