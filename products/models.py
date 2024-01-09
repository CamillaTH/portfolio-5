from django.db import models


class Category(models.Model):
    '''Model that holds information about categories'''
    name= models.CharField(max_length=270)
    user_friendly_name = models.CharField(max_length=270, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_user_friendly_name(self):
        return self.user_friendly_name

class ProductModel(models.Model):
    '''Model that holds information about products'''
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=270)
    description = models.TextField()
    sku = models.CharField(max_length=270, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
