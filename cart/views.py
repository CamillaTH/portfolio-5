from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import AddToCartForm
from products.models import Product

# Create your views here

def cart(request):
    """ View that shows the shopping cart page """
    
    return render(request, 'cart/cart.html')



@require_POST
def add_to_cart(request, product_id):
    print("sadsadsads")
    print(request.POST)
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    print(redirect_url)

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
    
    request.session['cart'] = cart
    print(request.session['cart'])
    # redirect_url is null of some reason need to be investigated
    #return redirect(redirect_url)

