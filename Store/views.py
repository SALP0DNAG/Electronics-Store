from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . import models
from . import forms


def index(request):
    context = {
        'categories': models.ProductCategory.objects.all()[:8],
        'special_products': models.SpecialProducts.objects.all(),
    }
    id_products = list()
    for special_product in context['special_products']:
        limit = 0
        for product in models.Product.objects.all():
            if product.category == special_product.category:
                id_products.append(product.pk)
                limit += 1
            if limit == 4:
                break
    context['products'] = models.Product.objects.filter(id__in=id_products)
    return render(request, 'Store/index.html', context=context)


def compares(request):
    return render(request, 'Store/compares.html')


def favorites(request):
    return render(request, 'Store/favorites.html')


@login_required
def basket(request):
    if request.method == 'POST':
        promocode_form = forms.PromocodeForm(request.POST)
        if promocode_form.is_valid():
            pass
    promocode_form = forms.PromocodeForm()
    baskets = models.Basket.objects.filter(user=request.user)
    total_sum = sum(basket.sum() for basket in baskets)
    context = {
        'baskets': baskets,
        'promocode_form': promocode_form,
        'total_sum': total_sum
    }
    return render(request, 'Store/basket.html', context)


@login_required
def basket_add(request, product_id):
    product = models.Product.objects.get(id=product_id)
    baskets = models.Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        basket = models.Basket(user=request.user, product=product)
        basket.save()
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_minus(request, basket_id):
    basket = models.Basket.objects.get(id=basket_id)
    if basket.quantity > 1:
        basket.quantity -= 1
        basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_delete(request, basket_id):
    basket = models.Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
