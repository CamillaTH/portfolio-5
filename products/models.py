from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    '''Model that holds information about categories'''

    class Meta:
        verbose_name_plural= 'Categories'
        
    name= models.CharField(max_length=270)
    user_friendly_name = models.CharField(max_length=270, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_user_friendly_name(self):
        return self.user_friendly_name

class Product(models.Model):
    '''Model that holds information about products'''
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=270)
    description = models.TextField()
    sku = models.CharField(max_length=270, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    '''Model to store reviews for products'''
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f'Review for {self.product.name} by {self.user.username}'

    class Meta:
        ''' Make sure user can leave only 1 review on each product '''
        unique_together = ('product', 'user')     