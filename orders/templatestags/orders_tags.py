from django import template
from orders import models

register = template.Library()


@register.simple_tag()
def get_order_cost(request, order_id):
    order_cost = sum(i.get_total_price() for i in models.OrderItem.objects.filter(order=order_id))
    if models.Order.objects.get(id=order_id).delivery_method == 'pickup':
        return order_cost
    return order_cost + 300


@register.simple_tag()
def get_cost_all_orders(request):
    cost_all_orders = sum(get_order_cost(request, i.id) for i in models.Order.objects.filter(user=request.user))
    return cost_all_orders
