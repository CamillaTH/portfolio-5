from django.contrib import admin
from .models import Product, Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'user_friendly_name',
        'name',
    )

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'rating',
        'category',
        'image',
        'price',
    )

    ordering = ('sku',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)