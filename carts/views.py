from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Cart, CartItem
from products.models import Product


def view(request):
    exist = 'exist'
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None

    if the_id:
        new_total = 0.00
        for item in cart.cartitem_set.all():
            line_total = float(item.product.price) * item.quantity
            new_total += line_total

        request.session['items_total'] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()
        context = {'cart': cart, 'exist': exist}
    else:
        empty_message = 'Your Cart is Empty'
        context = {'empty': True, 'exist': exist,
                   'empty_message': empty_message}

    template = 'carts/cart.html'
    return render(request, template, context)

def remove_from_cart(request, id):
    try:
        try:
            the_id = request.session['cart_id']
            cart = Cart.objects.get(id=the_id)
        except:
            return HttpResponseRedirect(reverse('cart'))

        cartitem = CartItem.objects.get(id=id)
        cartitem.cart = None
        cartitem.save()
        return HttpResponseRedirect(reverse('cart'))
    except:
        return HttpResponseRedirect(reverse('cart'))

def add_to_cart(request, slug):
    request.session.set_expiry(120000)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass

    if request.method == "POST":
        qty = request.POST['qty']
        for item in request.POST:
            key = item
            val = request.POST[key]

        cart_item = CartItem.objects.create(cart=cart, product=product)
        cart_item.quantity = qty
        cart_item.save()
                
        
        return HttpResponseRedirect(reverse('cart'))
    return HttpResponseRedirect(reverse('cart'))
