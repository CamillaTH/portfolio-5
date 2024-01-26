from django.shortcuts import render

# Create your views here

def cart(request):
    """ View that shows the shopping cart page """
    
    return render(request, 'cart/cart.html')