from django.shortcuts import render


def about_us(request):
    return render(request, 'page/about_us.html')


def payment(request):
    return render(request, 'page/payment.html')


def delivery(request):
    return render(request, 'page/delivery.html')


def contacts(request):
    return render(request, 'page/contacts.html')


def news(request):
    return render(request, 'page/news.html')


def requisites(request):
    return render(request, 'page/requisites.html')


def vacancies(request):
    return render(request, 'page/vacancies.html')


def how_to_order(request):
    return render(request, 'page/how_to_order.html')


def discounts_and_bonuses(request):
    return render(request, 'page/discounts_and_bonuses.html')


def return_of_goods(request):
    return render(request, 'page/return_of_goods.html')


def bulk_orders(request):
    return render(request, 'page/bulk_orders.html')


def suppliers(request):
    return render(request, 'page/suppliers.html')
