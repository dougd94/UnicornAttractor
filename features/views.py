from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Feature, Commentf, Votesf
from .forms import FeatureForm, CommentForm



def all_features(request):
    features = Feature.objects.filter(paid=True).filter(created_date__lte=timezone.now()
        ).order_by('-upvotes')
    return render(request, "features.html", {"features": features})
    

def feature_detail(request, pk):
    """
    feature pages
    """
    feature = get_object_or_404(Feature, pk=pk)
    feature.views += 1
    feature.save()
    # filter comments commentf = comment for features
    comments = Commentf.objects.filter(feature=feature).order_by('-created_date')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content=request.POST.get('content')
            comment = Commentf.objects.create(feature=feature, author=request.user, content=content)
            comment.save()
    else:
        comment_form=CommentForm()
            
    context =  { 
        'feature' : feature, 
        'comments' : comments,
        'comment_form' : comment_form,
    }
    
    return render(request, "featuredetail.html", context)
    
@login_required 
def create_feature(request, pk=None):
    """
    create a feature 
    """
    feature = get_object_or_404(Feature, pk=pk) if pk else None
    if request.method == "POST":
        form = FeatureForm(request.POST)
        # if its valid continue with this
        if form.is_valid():
            feature=form.save(commit=False)
            feature.author_id = request.user.id
            feature.price = 50
            feature.save()
            
            
            cart = request.session.get('cart', {})
            id = feature.pk
            cart[id] = cart.get(id, 1)
            request.session['cart'] = cart
        
            return redirect(feature_detail, feature.pk)
    else:
        form = FeatureForm(instance=feature)
    return render(request, 'featureform.html', {'form': form})

@login_required
def feature_upvote(request, feature_id):
    """
    feature upvote
    """
    voterf=request.user.id
    feature = Feature.objects.get(pk=feature_id)
    check = Votesf.objects.filter(feature=feature, voterf=voterf)
    # if its paid it must be an upvote so price changes to 5.00
    if feature.paid == True:
        feature.price = 5.00
        feature.save()
        cart = request.session.get('cart', {})
        id = feature.pk
        cart[id] = cart.get(id, 1)
        request.session['cart'] = cart
        messages.success(request, 'Upvote added to cart', extra_tags="alert-success")
        return redirect(feature_detail, feature.pk)
    # this just catches people from upvoting before its payed for, although the upvote is hidden in this case
    else: 
        messages.error(request, 'You can not upvote before paying!', extra_tags='alert-danger')
        return redirect(feature_detail, feature.pk)