from django.urls import path, include, re_path
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.views import serve
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from home.views import custom_404_view, custom_500_view
from user.views import account_page, add_to_wishlist , remove_from_wishlist
from .sitemaps import CustomSitemap

handler404 = custom_404_view

handler500 = custom_500_view

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
    path('account/', account_page, name='account_page'),
    path('add_to_wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:product_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^robots.txt$', serve, {'path': 'robots.txt'}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)