from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderEntry

@receiver(post_save, sender=OrderEntry)
def update_on_save(sender, created, instance, **kwargs):
    ''' update  subtotal on orderEntry creation/update'''
    instance.order.update_total_price()


@receiver(post_delete, sender=OrderEntry)
def update_on_save(sender, instance, **kwargs):
    ''' update  subtotal on orderEntry delete'''
    instance.order.update_total_price()