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
        'stripe_public_key': 'pk_test_51OdKSMAf4obymTxj7wy2j3e9yC8RGV7ZryVFJTMqIr4bPtOZDiiAD6IS32depUKbmdMngXmLPpO9wyEyHdTZ06yL00Gul5FQeT',
        'stripe_client_secret': 'sk_test_51OdKSMAf4obymTxjSFXa2YVcb3EtiLDy9xJOcjA1v2gvoPgkdd1LsdVvR6sYKadWbZGVMUvp1PginrzTek3OJZBU00MIkB94Of',
    }

    return render(request, 'checkout/checkout.html', context)