from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    city = models.CharField(max_length=30, blank=True)
    address = models.TextField(max_length=250, blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


