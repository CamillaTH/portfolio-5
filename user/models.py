from django.db import models
from django.contrib.auth.models import User, AbstractUser
from cloudinary.models import CloudinaryField
from products.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

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
        return f"Wishlist for {self.user.username}"

class SiteMessage(models.Model):
    ''' Model that stores messages employees can show the users '''
    location_choices = (
        ('HEADER', 'Header'),
        ('CART', 'Cart'),
    )
    location = models.CharField(max_length=10, choices=location_choices, unique=True)
    message = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.location} Message"

class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20,
                                            null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40,
                                            null=True, blank=True)
    default_county = models.CharField(max_length=80,
                                      null=True, blank=True)
    default_postcode = models.CharField(max_length=20,
                                        null=True, blank=True)
    default_country = CountryField(blank_label='Country',
                                   null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()