from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Bug, Comment, Votes
from .forms import BugForm, CommentForm


# Create your views here.
# show all bugs
def all_bugs(request):
    bugs = Bug.objects.filter(created_date__lte=timezone.now()
        ).order_by('-upvotes')
    return render(request, "bugs.html", {"bugs": bugs})
    
@login_required 
def bug_detail(request, pk):
    """
    bug pages
    """
    bug = get_object_or_404(Bug, pk=pk)
    # views iterate up by one every viewing.
    bug.views += 1
    bug.save()
    comments = Comment.objects.filter(bug=bug).order_by('-created_date')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content=request.POST.get('content')
            comment = Comment.objects.create(bug=bug, author=request.user, content=content)
            comment.save()
    else:
        comment_form=CommentForm()
            
    context =  { 
        'bug' : bug, 
        'comments' : comments,
        'comment_form' : comment_form,
    }
    
    return render(request, "bugdetail.html", context)

@login_required
def bug_upvote(request, bug_id):
    """
    bug upvote
    """
    voter=request.user.id
    bugpk = Bug.objects.get(pk=bug_id)
    # if user has voted on it already no upvote
    check = Votes.objects.filter(bugpk=bugpk, voter=voter)
    if not check:
        check = Votes(bugpk = bugpk, voter_id = request.user.id)
        check.save()
        bugpk.upvotes += 1
        bugpk.save()
        return redirect(reverse('bugs'))
    else: 
        messages.error(request, 'You have already upvoted that!', extra_tags="alert-danger")
        return redirect(reverse('bugs'))

        
        
  
@login_required 
def create_bug(request, pk=None):
    """
    create a bug 
    """
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if request.method == "POST":
        form = BugForm(request.POST,request.FILES, instance=bug)
        if form.is_valid():
            bug_group= form.save(commit=False)
            #get the author
            bugauthor_id = request.user.id
            bug_group.author_id = bugauthor_id
            bug_group = form.save()
            return redirect(bug_detail, bug_group.pk)
    else:
        form = BugForm(instance=bug)
    return render(request, 'bugform.html', {'form': form})