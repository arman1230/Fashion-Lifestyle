from atexit import register
from django import template

register=template.Library()

@register.filter(name="cart_quantity")
def cart_quantity(product,cart):
    keys=cart.keys()
    for ids in keys:
        if int(ids)==product.id:
            return cart[ids]
    return 0;