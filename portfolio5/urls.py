from django.urls import path, include, re_path
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.views import serve
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from home.views import custom_404_view
from .sitemaps import CustomSitemap

handler404 = custom_404_view

sitemaps = {
    'custom': CustomSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^robots.txt$', serve, {'path': 'robots.txt'}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)