from django.contrib.sitemaps import Sitemap
from products.models import Product
from django.urls import reverse

class CustomSitemap(Sitemap):
    ''' custom sitemap '''
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Product.objects.all()

    def location(self, item): 
        return reverse('product_detail', args=[str(item.id)])

    def lastmod(self, obj):
        return obj.last_updated

    #plan is to use image url in the custom sitemap when i can make it to work
    def image(self, obj):
        return obj.image_url

    #plan is to use name url in the custom sitemap when i can make it to work
    def name(self, obj):
        return obj.name

    #plan is to use rating url in the custom sitemap when i can make it to work
    def rating(self, obj):
        return obj.rating

    ##plan is to use category_name url in the custom sitemap when i can make it to work
    def category_name(self, obj):
        return obj.category.name

    def items(self):
        return Product.objects.all()

    #def location(self, item):
    #    return reverse('product_detail', args=[str(item.id)])