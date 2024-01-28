from django.shortcuts import render


def orders(request):
    return render(request, 'users/orders.html')


def address(request):
    return render(request, 'users/address.html')


def discounts_and_bonuses(request):
    return render(request, 'users/discounts-and-bonuses.html')


def contacts(request):
    return render(request, 'users/contacts.html')


def login(request):
    return render(request, 'users/login.html')


def register(request):
    return render(request, 'users/register.html')
