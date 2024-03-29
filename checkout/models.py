from django.db import models
from products.models import Product
from django.conf import settings
from django.db.models import Sum
import random
from datetime import date

class Order(models.Model):
    ''' Model that holds information about orders '''
    order_number = models.CharField(max_length=20, null=False, editable=False)
    email = models.CharField(max_length=30, null=False, blank=False)
    phone = models.CharField(max_length=12, null=False, blank=False)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=40, null=False, blank=False)
    full_name = models.CharField(max_length=70, null=True, blank=True)
    postal_code = models.CharField(max_length=5, null=True, blank=True)
    street_address = models.CharField(max_length=100, null=False, blank=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    date = models.DateTimeField(auto_now=True)
    country = models.CharField(max_length=45, null=True, blank=True)
    city = models.CharField(max_length=45, null=True, blank=True)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    original_cart = models.TextField(null=False, blank=False, default='')
    
    def save(self, *args, **kwargs):
        ''' overrides original savemethod produces a unique 16-digit order number with the last 8 digits as the order date'''
        unique_order_number = self.generate_order_number()
        self.order_number = unique_order_number

        if self.first_name and self.last_name:
            self.full_name = f'{self.first_name} {self.last_name}'
        else:
            self.full_name = ""

        super().save(*args, **kwargs)

    def generate_order_number(self):
        ''' produce the first 8 digits (random numbers) '''
        random_part = ''.join(str(random.randint(0, 9)) for _ in range(9))

        # produce the last 8 digits as the order date in the format YYYYMMDD
        order_date_part = date.today().strftime("%Y%m%d")

        # Combine both parts to form the 16-digit order number
        order_number = f"{random_part}-{order_date_part}"
        return order_number

    def update_total(self):
        ''' updates and calculates total price every time an orderEntry is added '''
    
        self.subtotal = self.orderEntries.aggregate(
            Sum('entry_total'))['entry_total__sum'] or 0
        if self.subtotal < settings.FREE_SHIPPING_THRESHOLD:
            self.shipping_cost = settings.STANDARD_SHIPPING_PRICE
        else:
            self.delivery_cost = 0
        self.total_price = self.subtotal + self.shipping_cost
        self.save()

    def __str__(self):
        return self.order_number

class OrderEntry(models.Model):
    ''' Model that holds information about order entires '''
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='orderEntries')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    entry_total = models.DecimalField(max_digits=6, null=False, blank=False, editable=False, decimal_places=2)

    def save(self, *args, **kwargs):
        ''' overries original save method and calculate entry price'''
        self.entry_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} _ {self.order.order_number}'


