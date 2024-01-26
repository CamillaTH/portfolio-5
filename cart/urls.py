from django.urls import path, include
from . import views
from .views import add_to_cart

urlpatterns = [
    path('', views.cart, name="view_cart"),
    path('add_to_cart/<product_id>/', add_to_cart, name='add_to_cart'),
]
