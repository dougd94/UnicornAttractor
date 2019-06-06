from django.shortcuts import render, redirect, reverse
from  features.models import Feature
# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified feature to the cart"""
    # quantity = Feature.quantity
    # #int(request.POST.get('quantity'))

    # cart = request.session.get('cart', {})
    # cart[id] = cart.get(id)
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        cart[id] = 1
        request.session['cart'] = cart

    # request.session['cart'] = cart
        return redirect(reverse('index'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified feature to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))