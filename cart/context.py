from django.conf import settings

def cart_items(request):
    """ cart items context processor """

    cart_items = []
    subtotal = 0
    products_count = 0

    if subtotal < settings.FREE_SHIPPING_THRESHOLD:
        free_shipping_detla = settings.FREE_SHIPPING_THRESHOLD - subtotal
        shipping = settings.STANDARD_SHIPPING_PRICE
    else:
        free_shipping_detla = 0
        shipping = 0

    total_price = shipping + subtotal

    context = {
        'total_price': total_price,
        'subtotal' : subtotal,
        'shipping' : shipping,
        'cart_items' : cart_items,
        'free_shipping_detla' : free_shipping_detla,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
    }

    return context