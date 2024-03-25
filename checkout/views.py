from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from cart.context import cart_entries
from products.models import Product
from .models import Order, OrderEntry
from django.core.mail import send_mail
from django.template.loader import render_to_string

from products.models import Product
from user.models import UserProfile
from user.forms import UserProfileForm

import stripe
import json

def checkout(request):
    """ View that shows the checkout page and validates cart exists and have entries and post orders"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'country': request.POST['country'],
            'postal_code': request.POST['postal_code'],
            'city': request.POST['city'],
            'street_address': request.POST['street_address'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            print("orderform valid")
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_entry_item = OrderEntry(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_entry_item.save()
                    else:
                        for size, quantity in item_data['entries_by_size'].items():
                            order_entry_item = OrderEntry(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_entry_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't "
                        "found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))
            
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))

        else:
            messages.error(request, ('There was an error in the form.'
                                     'Please double check your information.'))

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
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone,
                    'country': profile.default_country,
                    'postal_code': profile.default_postcode,
                    'city': profile.default_city,
                    'street_address': profile.default_street_address,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to add it?')

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'stripe_client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """ Handle successful checkout """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    
    #send order confirmation
    print("sending order confirmation")
    print(order.total_price)
    send_confirmation_email(order)

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order.user_profile = profile
            order.save()

            # Save the user's info
            if save_info:
                profile_data = {
                    'default_phone': order.phone,
                    'default_country': order.country,
                    'default_postcode': order.postal_code,
                    'default_city': order.city,
                    'default_street_address': order.street_address,
                }
                user_profile_form = UserProfileForm(profile_data, instance=profile)
                if user_profile_form.is_valid():
                    user_profile_form.save()
        except UserProfile.DoesNotExist:
            # Handle the case where UserProfile does not exist for the user
            # You can log the error, display a message to the user, or take any other appropriate action
            print("UserProfile does not exist for the authenticated user.")


    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

def send_confirmation_email(order):
        """Send the user a confirmation email"""
        print("seeeeeeeeeeeeeeeeeeeeeeeeeeeendEmail")
        cust_email = order.email
        subject = render_to_string(
            'checkout/emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )


@require_POST
def cache_checkout_data(request):
    print(request.POST.get('save_info'))
    print(request.user)
    print(json.dumps(request.session.get('cart', {})))
    return HttpResponse(status=200)
    '''
    Stripe always responds with 400 bad request and havent found any solution why...
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=e, status=400)'''