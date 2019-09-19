from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from carts.models import Cart
from .models import Order
from .utils import id_generator
#from datetime import datetime
#import time
# Create your views here.


def orders(request):
    context = {}
    template = "orders/user.html"
    return render(request, template, context)

#requires user login
@login_required
def checkout(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse('cart'))

    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.save()
    except:
        return HttpResponseRedirect(reverse('cart'))

    # new_order, created = Order.objects.get_or_create(cart=cart)
    # if created:
    #     new_order.order_id = id_generator()
    # new_order.user = request.user
    # new_order.save()

    if new_order.status == "Finished":
        #this deletes the cart
        #cart.delete()
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse('cart'))

    context = {}
    template = "orders/checkout.html"
    return render(request, template, context)
