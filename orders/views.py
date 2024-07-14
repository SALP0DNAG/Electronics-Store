from django.shortcuts import render
from . import models as orders_models
from Store import models as store_models
from django.shortcuts import redirect
from .models import Order
from django.contrib.auth.decorators import login_required


@login_required
# Create your views here.
def new_order(request):
    user = request.user
    baskets = store_models.Basket.objects.filter(user=request.user)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        payment_method = request.POST.get('pay_method')
        delivery_method = request.POST.get('delivery_method')
        address = request.POST.get('city') + ' ' + request.POST.get('address')
        phone_number = request.POST.get('number')
        recipient = request.POST.get('full_name')
        order = orders_models.Order.objects.create(comment=comment, user=user, payment_method=payment_method,
                                                   delivery_method=delivery_method, address=address,
                                                   phone_number=phone_number,
                                                   recipient=recipient)
        for basket in baskets:
            orders_models.OrderItem.objects.create(order=order, product=basket.product, quantity=basket.quantity)
            basket.delete()
        return redirect('orders:order', order_id=order.id)
    total_sum = sum(basket.sum() for basket in baskets)
    context = {
        'user': user,
        'baskets': baskets,
        'total_sum': total_sum,
    }
    return render(request, 'orders/new_order.html', context=context)


@login_required
def order(request, order_id):
    order = orders_models.Order.objects.get(id=order_id)
    items = order.items.all()
    order_cost = sum(position.get_total_price() for position in items)
    if order.delivery_method == 'courier':
        order_cost += 300
    context = {
        'order': order,
        'items': items,
        'order_cost': order_cost,
        'status': dict(Order.STATUS_CHOICES)[order.status],
        'payment_method': dict(Order.PAYMENT_CHOICES)[order.payment_method],
        'delivery_method': dict(Order.DELIVERY_CHOICES)[order.delivery_method],

    }
    return render(request, 'orders/order.html', context=context)
