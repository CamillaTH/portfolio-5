from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    """ View that shows the checkout page and validates cart exists and have entries"""
    
    cart = request.session.get('cart', {})
    cart_entries = request.session.get('cart_entries', [])
    if not cart and not cart_entries:
        messages.error(request, 'Your cart is empty')
        return redirect(reverse('products'))

    order_form = OrderForm()

    context = {
        'order_form': order_form,
    }

    return render(request, 'checkout/checkout.html', context)