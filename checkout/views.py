from django.shortcuts import render, redirect
#from checkout.models import Order

# Create your views here

def checkout(request):
    """ View that shows the checkout page """
    
    cart = request.session.get('cart', {})

    return render(request, 'checkout/checkout.html')