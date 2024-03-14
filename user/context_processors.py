from .models import SiteMessage
from django.core.exceptions import ObjectDoesNotExist

def site_messages(request):
    """ Context processor to add site messages to the context """
    header_message = None
    cart_message = None

    try:
        header_message = SiteMessage.objects.get(location='HEADER')
        cart_message = SiteMessage.objects.get(location='CART')
    except ObjectDoesNotExist:
        pass

    return {
        'header_message': header_message,
        'cart_message': cart_message,
    }