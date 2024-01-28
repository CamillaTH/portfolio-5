from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from cart.context import cart_entries
import stripe

def checkout(request):
    """ View that shows the checkout page and validates cart exists and have entries and post orders"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        
    else: # form not submitted get checkout data an init payment
        cart = request.session.get('cart', {})
        cart_items = request.session.get('cart_entries', [])
        if not cart and not cart_items:
            messages.error(request, 'Your cart is empty')
            return redirect(reverse('products'))

        current_cart = cart_entries(request)
        total_price = current_cart['total_price']
        stripe_total = round(total_price * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )
        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to add it?')

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'stripe_client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)