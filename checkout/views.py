from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from features.models import Feature, Votesf
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


@login_required
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                feature = get_object_or_404(Feature, pk=id)
                total += quantity * feature.price
                order_line_item = OrderLineItem(
                    order=order,
                    feature=feature,
                    quantity=quantity
                )
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!", extra_tags='alert_danger')
            
            if customer.paid:
                for id, quantity in cart.items():
                    if feature.paid == False:
                        feature.paid = True
                    if feature.paid == True:
                            feature.upvotes += 1
                feature.save()
                messages.success(request, "You have successfully paid", extra_tags='alert-success')
                request.session['cart'] = {}
                return redirect(reverse('features'))
            else:
                messages.error(request, "Unable to take payment", extra_tags="alert-danger")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!", extra_tags="alert-danger")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})