from django import template

register = template.Library()


@register.filter
def cart_total(cart):
    return sum(float(item['price']) * int(item['quantity']) for item in cart.values())
