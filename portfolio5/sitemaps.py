from django.contrib.sitemaps import Sitemap
from products.models import Product
from django.urls import reverse

class CustomSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Product.objects.all()

    def location(self, item):
        return reverse('product_detail', args=[str(item.id)])

    def lastmod(self, obj):
        return obj.last_updated

    def image(self, obj):
        return obj.image_url

    def name(self, obj):
        return obj.name

    def rating(self, obj):
        return obj.rating

    def category_name(self, obj):
        return obj.category.name

    def items(self):
        return Product.objects.all()

    def location(self, item):
        return reverse('product_detail', args=[str(item.id)])