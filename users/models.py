from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    city = models.CharField(max_length=30, blank=True)
    address = models.TextField(max_length=250, blank=True)
    phone_number = PhoneNumberField(unique=False, blank=True)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.username} | {self.email}'