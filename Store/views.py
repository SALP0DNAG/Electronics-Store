from django.shortcuts import render
from . import models


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
