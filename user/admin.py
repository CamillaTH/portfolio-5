from django.contrib import admin

from .models import SiteMessage
from .models import UserProfile, Wishlist
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# Defines an inline admin for Wishlist
class WishlistInline(admin.StackedInline):
    model = Wishlist
    can_delete = False
    verbose_name_plural = 'Wishlist'


# Define a new UserAdmin class
class UserAdmin(BaseUserAdmin):
    inlines = (WishlistInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(SiteMessage)
