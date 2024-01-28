from django.urls import path, include
from . import views
#from .views import 

urlpatterns = [
    path('', views.checkout, name="checkout"),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
]
