from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from . import forms


def orders(request):
    return render(request, 'users/orders.html')


def address(request):
    return render(request, 'users/address.html')


def discounts_and_bonuses(request):
    return render(request, 'users/discounts-and-bonuses.html')


def contacts(request):
    return render(request, 'users/contacts.html')


def login(request):
    if request.method == 'POST':
        form = forms.UserLoginForm(data=request.POST)
        if form.is_valid():
            print(request.POST)
            email = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:orders'))
    else:
        form = forms.UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context=context)


def register(request):
    return render(request, 'users/register.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('store:index'))
