from django.urls import path, include
from . import views
from .views import add_to_cart

urlpatterns = [
    path('', views.checkout, name="view_checkout"),
]
