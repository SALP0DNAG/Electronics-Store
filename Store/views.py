from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
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


@login_required
def compares(request):
    return render(request, 'Store/compares.html')


@login_required
def favorites(request):
    products = models.Favorite.objects.filter(user=request.user)
    if request.method == 'POST':
        sort_form = forms.SortFormFavorites(request.POST)
        if request.POST['sort_by'] == 'price_increase':
            products = products.order_by('product__price')
        elif request.POST['sort_by'] == 'price_drop':
            products = products.order_by('-product__price')
        elif request.POST['sort_by'] == 'data_addition':
            products = products.order_by('-created_timestamp')
    else:
        sort_form = forms.SortFormFavorites()
    context = {
        'favorites': products,
        'sort_form': sort_form,
    }
    return render(request, 'Store/favorites.html', context=context)


@login_required
def favorites_add(request, product_id):
    product = models.Product.objects.get(id=product_id)
    models.Favorite.objects.create(user=request.user, product=product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def favorites_delete(request, product_id):
    product = models.Product.objects.get(id=product_id)
    models.Favorite.objects.get(product=product).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket(request):
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


def category(request, category_name):
    sort_form = forms.SortFormProducts()
    category_obj = models.ProductCategory.objects.get(name=category_name)
    products = models.Product.objects.filter(category=category_obj.id)
    if request.method == 'POST':
        sort_form = forms.SortFormProducts(request.POST)
        if request.POST['sort_by'] == 'price_increase':
            products = models.Product.objects.filter(category=category_obj.id).order_by('price')
        elif request.POST['sort_by'] == 'price_drop':
            products = models.Product.objects.filter(category=category_obj.id).order_by('-price')
    context = {
        'category_name': category_obj.name,
        'products': products,
        'sort_form': sort_form,
    }
    return render(request, 'Store/category.html', context=context)


def category_all(request):
    products = models.Product.objects.all()
    form = forms.SortForm()
    if request.method == 'POST':
        form = forms.SortForm(request.POST)
        if request.POST['sort_by'] == 'price_increase':
            products = models.Product.objects.all().order_by('price')
        elif request.POST['sort_by'] == 'price_drop':
            products = models.Product.objects.all().order_by('-price')
    context = {
        'category_name': 'Все категории',
        'products': products,
        'sort_form': form
    }
    return render(request, 'Store/category.html', context=context)


def product(request, category_name, product_id):
    product = models.Product.objects.get(id=product_id)
    context = {
        'product': product,
        'category_name': category_name
    }
    return render(request, 'Store/product.html', context=context)


def search(request):
    query = request.GET.get('query', '')
    products = models.Product.objects.filter(name__icontains=query) if query else []
    form = forms.SearchForm()
    context = {
        'form': form,
        'products': products,
        'query': query
    }
    return render(request, 'Store/search.html', context=context)
