from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages
from . import forms, models
from orders import models as orders_models


def orders(request):
    context = {
        'orders': orders_models.Order.objects.filter(user=request.user),
    }
    return render(request, 'users/orders.html', context=context)


def address(request):
    if request.method == 'POST':
        form = forms.AddressForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = forms.AddressForm(instance=request.user)
    context = {'form': form}
    return render(request, 'users/address.html', context)


def discounts_and_bonuses(request):
    return render(request, 'users/discounts-and-bonuses.html')


def contacts(request):
    if request.method == 'POST':
        form = forms.ContactsForm(data=request.POST, instance=request.user)
        if (models.User.objects.filter(email=request.POST['email']).exists() and
                request.user.email != request.POST['email']):
            messages.error(request, 'Почта с таким адресом уже существует')
        if (models.User.objects.filter(username=request.POST['username']).exists() and
                request.user.username != request.POST['username']):
            messages.error(request, 'Пользователь с таким именем уже существет')
        if form.is_valid():
            messages.success(request, "Пользователь успешно изменен")
            form.save()
    else:
        form = forms.ContactsForm(instance=request.user)
    context = {'form': form}
    return render(request, 'users/contacts.html', context)


def login(request):
    if request.method == 'POST':
        form = forms.UserLoginForm(data=request.POST)
        if form.is_valid():
            email = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:contacts'))
    else:
        form = forms.UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context=context)


def register(request):
    if request.method == 'POST':
        form = forms.UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = forms.UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('store:index'))
