from django.conf import settings
from products.models import Product
from django.shortcuts import get_object_or_404


def cart_entries(request):
    """Cart entries context processor"""

    cart = request.session.get('cart', {})
    cart_entries = []

    subtotal = sum(qty * get_object_or_404(Product, pk=entry_id).price for entry_id, qty in cart.items())
    products_count = sum(cart.values())

    free_shipping_delta = max(0, settings.FREE_SHIPPING_THRESHOLD - subtotal)
    shipping = settings.STANDARD_SHIPPING_PRICE if subtotal < settings.FREE_SHIPPING_THRESHOLD else 0

    total_price = shipping + subtotal

    for entry_id, qty in cart.items():
        product = get_object_or_404(Product, pk=entry_id)
        cart_entries.append({'entry_id': entry_id, 'qty': qty, 'product': product})

    context = {
        'total_price': total_price,
        'subtotal': subtotal,
        'shipping': shipping,
        'cart_entries': cart_entries,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
    }

    return context