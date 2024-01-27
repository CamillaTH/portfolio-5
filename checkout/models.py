from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=17, null=False, editable=False)
    email = models.CharField(max_length=30, null=False, blank=False)
    phone = models.CharField(max_length=12, null=False, blank=False)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=40, null=False, blank=False)
    postal_code = models.CharField(max_length=5, null=True, blank=True)
    street_address = models.CharField(max_length=100, null=False, blank=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # produce a unique 16-digit order number with the last 8 digits as the order date
        unique_order_number = self.generate_order_number()
        self.order_number = unique_order_number
        super().save(*args, **kwargs)

    def generate_order_number(self):
        # produce the first 8 digits (random numbers)
        rrandom_part = ''.join(str(random.randint(0, 9)) for _ in range(9))

        # produce the last 8 digits as the order date in the format YYYYMMDD
        order_date_part = date.today().strftime("%Y%m%d")

        # Combine both parts to form the 16-digit order number
        order_number = f"{random_part}-{order_date_part}"
        return order_number