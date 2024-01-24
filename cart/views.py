from django.shortcuts import render

# Create your views here

def index(request):
    """ View that shows the shopping bag page """
    
    return render(request, 'cart/cart.html')