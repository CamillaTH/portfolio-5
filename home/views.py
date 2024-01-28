from django.shortcuts import render
from django.contrib.sitemaps import Sitemap

# Create your views here

def index(request):
    """ View that returns the index page """
    
    return render(request, 'home/index.html')

def custom_404_view(request, exception):
    ''' render 404 page '''
    return render(request, '404.html', status=404)

class CustomSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return [
            '/',
            '/products/',
            '/cart/',
            '/checkout/',
            
        ]

    def location(self, item):
        return item