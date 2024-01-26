from django.conf import settings
from products.models import Product
from django.shortcuts import get_object_or_404
from decimal import Decimal

def cart_entries(request):
    """Cart entries context processor"""

    cart = request.session.get('cart', {})
    cart_entries = []

    subtotal = Decimal(sum(Decimal(qty) * get_object_or_404(Product, pk=entry_id).price for entry_id, qty in cart.items()))
    products_count = sum(cart.values())

    free_shipping_delta = max(Decimal(0), settings.FREE_SHIPPING_THRESHOLD - subtotal)
    shipping = settings.STANDARD_SHIPPING_PRICE if subtotal < settings.FREE_SHIPPING_THRESHOLD else Decimal(0)

    total_price = shipping + subtotal

    for entry_id, qty in cart.items():
        product = get_object_or_404(Product, pk=entry_id)
        entry_total_price = Decimal(product.price) * Decimal(qty)
        cart_entries.append({'entry_id': entry_id, 'qty': qty, 'product': product, 'entry_total_price': entry_total_price})

    context = {
        'total_price': total_price,
        'subtotal': subtotal,
        'shipping': shipping,
        'cart_entries': cart_entries,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': Decimal(settings.FREE_SHIPPING_THRESHOLD),
    }

    return context