from atexit import register
from django import template

register=template.Library()

@register.filter(name="cart_quantity")
def cart_quantity(product,cart):
    keys=cart.keys()
    for ids in keys:
        if int(ids)==product.id:
            return cart[ids]
    return 0

@register.filter(name="Calc")
def Calc(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id) == product.id:
            pr=product.dprice
            prc=int(pr[2:])
            return cart[id]*prc
    return 0

@register.filter(name="total")
def Calc(product,cart):
    keys=cart.keys()
    sum=0
    for id in keys:
        pr=product.dprice
        prc=int(pr[2:])
        sum=sum+cart[id]*prc
        return sum
    return 0