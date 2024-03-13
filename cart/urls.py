from django.urls import path, include
from . import views
from .views import add_to_cart

urlpatterns = [
    path('', views.cart, name="view_cart"),
    path('add_to_cart/<product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<item_id>/', views.remove_entry_from_cart, name='remove_entry_from_cart'),
    path('update_cart_quantity/<item_id>/', views.update_cart_quantity, name='update_cart_quantity'),
]
