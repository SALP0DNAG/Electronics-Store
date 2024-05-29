from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from . import models
from phonenumber_field.modelfields import PhoneNumberField


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'telephone-or-email-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password-input'}))

    class Meta:
        model = models.User
        fields = ('email', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'register-name-input'}))
    phone_number = PhoneNumberField()
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'register-email-input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'register-password-input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'register-password2-input'}))

    class Meta:
        model = models.User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')


class AddressForm(forms.ModelForm):
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-city'}), required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'input-address', 'rows': '3'}), required=False)

    class Meta:
        model = models.User
        fields = ('city', 'address')


class ContactsForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={}))
    phone_number = PhoneNumberField(error_messages=['Неправильный международный код или номер мобильного телефона!'],)
    email = forms.EmailField(widget=forms.EmailInput(attrs={}))

    class Meta:
        model = models.User
        fields = ('username', 'phone_number', 'email')
