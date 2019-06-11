from django.shortcuts import render, redirect, reverse
from  features.models import Feature
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def view_cart(request):
    """A View that renders the cart contents page"""
    
    return render(request, "cart.html")

@login_required
def add_to_cart(request, id):
    """Add a quantity of the specified feature to the cart"""
    # cart
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        cart[id] = 1
        request.session['cart'] = cart
        print(cart)
        return redirect(reverse('view_cart'))
   
    else:
        messages.error(request, 'Something went wrong!', extra_tags="alert-danger")
        return redirect(reverse('index'))

@login_required
def remove_cart(request, id):
    """
    Adjust the quantity of the specified feature to the specified
    amount
    """
    cart = request.session.get('cart', {})
    # pops feature from cart on click
    cart.pop(id)
    request.session['cart'] = cart
    
    return redirect(reverse('view_cart'))