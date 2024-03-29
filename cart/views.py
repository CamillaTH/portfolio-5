from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from products.models import Product

# Create your views here

def cart(request):
    """ View that shows the shopping cart page """
    
    return render(request, 'cart/cart.html')

@require_POST
def add_to_cart(request, product_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    product_size = None
    if 'product_size' in request.POST:
        print("siiize")
        print(product_size)
        product_size = request.POST['product_size']

    cart = request.session.get('cart', {})

    if product_size:
        if product_id in cart:
            if 'entries_by_size' not in cart[product_id]:
                cart[product_id]['entries_by_size'] = {}
            if product_size in cart[product_id]['entries_by_size']:
                cart[product_id]['entries_by_size'][product_size] += quantity
            else:
                cart[product_id]['entries_by_size'][product_size] = quantity
        else:
            cart[product_id] = {'entries_by_size': {product_size: quantity}}
    else:
        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity

    request.session['cart'] = cart

    messages.success(request, 'product added')

    return redirect(redirect_url)

def remove_entry_from_cart(request, item_id):
    """Remove the entry from the cart"""

    try:
        size = request.POST.get('product_size')
        cart = request.session.get('cart', {})

        if size:
            if item_id in cart and 'entries_by_size' in cart[item_id]:
                del cart[item_id]['entries_by_size'][size]
                if not cart[item_id]['entries_by_size']:
                    cart.pop(item_id)
            else:
                # Product doesn't have sizes, just remove it from the cart
                cart.pop(item_id, None)
        else:
            cart.pop(item_id, None)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

def update_cart_quantity(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['entries_by_size'][size] = quantity
        else:
            del cart[item_id]['entries_by_size'][size]
            if not cart[item_id]['entries_by_size']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect('view_cart')
