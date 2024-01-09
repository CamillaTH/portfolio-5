from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ View that show all prodcuts, sorting, searching """
    
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)