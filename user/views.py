from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import UserProfile, Wishlist
from products.models import Product

def account_page(request):
    user = request.user
    #user_profile = UserProfile.objects.get(user=user)
    wishlists = Wishlist.objects.filter(user=user)

    if request.method == 'POST':
        password_form = PasswordChangeForm(user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important for maintaining user's session
            return redirect('account_page')
    else:
        password_form = PasswordChangeForm(user)

    context = {
      #  'user_profile': user_profile,
        'wishlists': wishlists,
        'user': user,
        'password_form': password_form,
    }
    return render(request, 'account_page.html', context)

def add_to_wishlist(request, product_id):
    ''' Adds product to users wishlist '''
    if request.user.is_authenticated:
        product = Product.objects.get(pk=product_id)
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        if created:
            wishlist.products.add(product)
            wishlist.save()
        elif product not in wishlist.products.all():
            wishlist.products.add(product)
            wishlist.save()
        # Render the current product detail page again
        return render(request, 'products/product_detail.html', {'product': product})
    else:
        # Handle the case where the user is not authenticated
        return redirect('login')

def remove_from_wishlist(request, product_id):
    ''' Removes product from users wishlist '''
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        wishlist = Wishlist.objects.get(user=request.user)
        if product in wishlist.products.all():
            wishlist.products.remove(product)
            messages.success(request, 'Product removed from wishlist.')
        else:
            messages.error(request, 'Product is not in the wishlist.')
    return redirect('account_page')