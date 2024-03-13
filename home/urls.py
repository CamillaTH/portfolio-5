from django.contrib import admin
from django.urls import path, include
from . import views
from .views import index, subscribe_newsletter_view

urlpatterns = [
    path('', views.index, name="home"),
    path('subscribe-newsletter/', subscribe_newsletter_view, name='subscribe_newsletter'),
]