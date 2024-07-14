from django import template
from Store import models

register = template.Library()


@register.simple_tag
def get_total_quantity(request):
    if request.user.is_anonymous:
        total_quantity = 0
    else:
        baskets = models.Basket.objects.filter(user=request.user)
        total_quantity = sum(basket.quantity for basket in baskets)
    return total_quantity


@register.simple_tag
def product_in_favorites(request, product):
    if request.user.is_authenticated:
        return models.Favorite.objects.filter(user=request.user, product=product).exists()
    return False


@register.simple_tag
def favorites_exists(request):
    return models.Favorite.objects.filter(user=request.user).exists()



@register.filter
def desc_beginning(value, length):
    def len_list(list_words):
        return sum(len(i) for i in list_words)

    def max_words(value, length):
        list_words = value.split()
        lw = 0
        hi = len(list_words) - 1
        answer = ''
        while lw <= hi:
            md = (hi + lw) // 2
            if len_list(list_words[:md]) < length:
                answer = ' '.join(list_words[:md])
                lw = md + 1
            else:
                hi = md - 1
        return answer

    if len(value) > length:
        last_punctuation_mark = max(value[:length].rfind('.'), value[:length].rfind('!'), value[:length].rfind('?'))
        if last_punctuation_mark == -1:
            return max_words(value, length)
        else:
            return value[:last_punctuation_mark + 1]
    else:
        return value
