from django.contrib.auth.forms import AuthenticationForm
from django import forms
from . import models


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = models.User
        fields = ('email', 'password')


