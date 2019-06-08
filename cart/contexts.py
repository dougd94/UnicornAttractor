from django.shortcuts import get_object_or_404
from features.models import Feature


def cart_content(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    # id = request.POST['feature_id']
   
    need_to_pay = Feature.objects.filter(paid=False, author=request.user.id)
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    feature_count = 0
    
    for id, quantity in cart.items():
        feature = get_object_or_404(Feature, pk=id)
        # id=feature.id
        total += quantity * feature.price
        feature_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'feature': feature})
    
    if need_to_pay:
        for feature in need_to_pay:
            id = feature.id
            cart[id] = cart.get(id, 1)
            request.session['cart'] = cart
            
    return {'cart_items': cart_items, 'total': total, 'feature_count': feature_count}
    
   
    