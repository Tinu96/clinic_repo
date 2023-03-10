from .models import Cart,ServiceCart
from django.contrib.auth.models import AnonymousUser

def cart_count(request):
    count = 0
    if isinstance(request.user, AnonymousUser):
        return {}
    try:
        cart = Cart.objects.filter(user=request.user, status="in-cart")
    except Cart.DoesNotExist:
        return {}
    count=cart.count()
    context = {"cart_count": count}
    return context

def service_cart_count(request):
    count = 0
    if isinstance(request.user, AnonymousUser):
        return {}
    try:
        cart = ServiceCart.objects.filter(user=request.user, status="in-cart")
    except Cart.DoesNotExist:
        return {}
    count=cart.count()
    context = {"service_cart_count": count}
    return context