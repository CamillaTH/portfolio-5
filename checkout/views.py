from django.shortcuts import render, redirect
from products.models import Order

# Create your views here

def checkout(request):
    """ View that shows the checkout page """
    
    return render(request, 'checkout/checkout.html')