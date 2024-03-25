from django.conf import settings
from products.models import Product
from django.shortcuts import get_object_or_404
from decimal import Decimal

def cart_entries(request):
    """Cart entries context processor"""

    cart = request.session.get('cart', {})
    cart_entries = []

    subtotal = Decimal(0)
    products_count = 0  # init products_count as an integer

    for entry_id, entry_data in cart.items():
        if isinstance(entry_data, int):
            product = get_object_or_404(Product, pk=entry_id)
            entry_total_price = Decimal(product.price) * Decimal(entry_data)
            subtotal += entry_total_price
            cart_entries.append({'entry_id': entry_id, 'qty': entry_data, 'product': product, 'entry_total_price': entry_total_price, 'size': None})
            products_count += 1  # Increment products_count for each product entry
        else:
            product = get_object_or_404(Product, pk=entry_id)
            for size, qty in entry_data.get('entries_by_size', {}).items():
                entry_total_price = Decimal(product.price) * Decimal(qty)
                subtotal += entry_total_price
                cart_entries.append({'entry_id': entry_id, 'qty': qty, 'product': product, 'entry_total_price': entry_total_price, 'size': size})
                products_count += 1  # Increment products_count for each product entry

    free_shipping_delta = max(Decimal(0), settings.FREE_SHIPPING_THRESHOLD - subtotal)
    shipping = settings.STANDARD_SHIPPING_PRICE if subtotal < settings.FREE_SHIPPING_THRESHOLD else Decimal(0)

    total_price = shipping + subtotal

    context = {
        'total_price': total_price,
        'subtotal': subtotal,
        'shipping': shipping,
        'cart_entries': cart_entries,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': Decimal(settings.FREE_SHIPPING_THRESHOLD),
        'products_count': products_count,  # Include products_count in the context
    }

    return context

'''def cart_entries(request):
    """Cart entries context processor"""

    cart = request.session.get('cart', {})
    cart_entries = []

    subtotal = Decimal(0)
    products_count = 0  # init products_count as an integer

    for entry_id, entry_data in cart.items():
        if isinstance(entry_data, int):
            product = get_object_or_404(Product, pk=entry_id)
            entry_total_price = Decimal(product.price) * Decimal(entry_data)
            subtotal += entry_total_price
            cart_entries.append({'entry_id': entry_id, 'qty': entry_data, 'product': product, 'entry_total_price': entry_total_price})
            products_count += 1  # Increment products_count for each product entry
        elif isinstance(entry_data, dict):
            product = get_object_or_404(Product, pk=entry_id)
            for size, qty in entry_data.get('entries_by_size', {}).items():
                entry_total_price = Decimal(product.price) * Decimal(qty)
                subtotal += entry_total_price
                cart_entries.append({'entry_id': entry_id, 'qty': qty, 'product': product, 'entry_total_price': entry_total_price, 'size': size})
                products_count += 1  # Increment products_count for each product entry

    free_shipping_delta = max(Decimal(0), settings.FREE_SHIPPING_THRESHOLD - subtotal)
    shipping = settings.STANDARD_SHIPPING_PRICE if subtotal < settings.FREE_SHIPPING_THRESHOLD else Decimal(0)

    total_price = shipping + subtotal

    context = {
        'total_price': total_price,
        'subtotal': subtotal,
        'shipping': shipping,
        'cart_entries': cart_entries,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': Decimal(settings.FREE_SHIPPING_THRESHOLD),
        'products_count': products_count,  # Include products_count in the context
    }

    return context'''