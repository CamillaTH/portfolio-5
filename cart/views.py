from django.shortcuts import render, redirect
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
    return redirect(redirect_url)