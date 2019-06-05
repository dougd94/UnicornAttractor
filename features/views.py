from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Feature, Commentf
from .forms import FeatureForm, CommentForm
# from .forms import BugForm, CommentForm



def all_features(request):
    features = Feature.objects.filter(paid=True)
    return render(request, "features.html", {"features": features})
    

def feature_detail(request, pk):
    """
    feature pages
    """
    feature = get_object_or_404(Feature, pk=pk)
    feature.views += 1
    feature.save()
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
def create_or_edit_feature(request, pk=None):
    """
    create a feature 
    """
    feature = get_object_or_404(Feature, pk=pk) if pk else None
    if request.method == "POST":
        form = FeatureForm(request.POST,request.FILES, instance=feature)
        if form.is_valid():
            feature_group= form.save(commit=False)
            #get the author
            featureauthor_id = request.user.id
            feature_group.author_id = featureauthor_id
            feature_group = form.save()
            return redirect(feature_detail, feature_group.pk)
    else:
        form = FeatureForm(instance=feature)
    return render(request, 'featureform.html', {'form': form})

# @login_required
# def bug_upvote(request, bug_id):
#     """
#     bug upvote
#     """
#     voter=request.user.id
#     bugpk = Bug.objects.get(pk=bug_id)
#     check = Votes.objects.filter(bugpk=bugpk, voter=voter)
#     if not check:
#         check = Votes(bugpk = bugpk, voter_id = request.user.id)
#         check.save()
#         bugpk.upvotes += 1
#         bugpk.save()
#         return redirect(reverse('bugs'))
#     else: 
#         messages.error(request, 'You have already upvoted that!', extra_tags="alert-danger")
#         return redirect(reverse('bugs'))