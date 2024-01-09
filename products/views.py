from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.

def all_products(request):
    """ View that shows all products, sorting, searching """
    
    products = Product.objects.all()
    query = None
    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                print("noooooting")
                messages.error(request, "You did not enter any search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    print(products.query)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ View that show the product detail page"""
    
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)