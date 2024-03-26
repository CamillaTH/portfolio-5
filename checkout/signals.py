from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderEntry

@receiver(post_save, sender=OrderEntry)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on orderEntry update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderEntry)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on orderEntry delete
    """
    instance.order.update_total()