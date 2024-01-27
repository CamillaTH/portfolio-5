from django.db import models
from django.contrib.auth.models import User, AbstractUser
from cloudinary.models import CloudinaryField
from products.models import Product

class ExtendedUser(models.Model):
    '''Model that have one2one rel with user with custom fields'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileImage = CloudinaryField('image', default='placeholder')

    def __str___(self):
        return self.user.username

    def get_profile_image(self):
        return self.profileImage.url

class Wishlist(models.Model):
    ''' Model that stores users wishlist with products '''
    user = models.OneToOneField(ExtendedUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"Wishlist for {self.user.user.username}"