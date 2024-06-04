from django import template
from Store import models


register = template.Library()


@register.simple_tag()
def get_total_quantity(request):
    if request.user.is_anonymous:
        total_quantity = 0
    else:
        baskets = models.Basket.objects.filter(user=request.user)
        total_quantity = sum(basket.quantity for basket in baskets)
    return total_quantity

