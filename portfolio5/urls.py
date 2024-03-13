from django.urls import path, include, re_path
from django.urls.base import reverse  # Import reverse from django.urls.base
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from datetime import datetime
from django.contrib.staticfiles.views import serve
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from products.models import Product
from home.views import custom_404_view

handler404 = custom_404_view

class CustomSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        
        return Product.objects.all()
        
      #  return [
       #     'home',
        #    'products',
        #    'view_cart',
        #    'checkout',
        #]

    def location(self, item):
        return 'product_id/' + str(item.pk)

    def lastmod(self, obj):
        return datetime.now()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': {'custom': CustomSitemap}, 'template_name': 'sitemap.xml.template'}),
    re_path(r'^robots.txt$', serve, {'path': 'robots.txt'}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)