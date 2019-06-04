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
        ).order_by('-created_date')
    return render(request, "bugs.html", {"bugs": bugs})
    
@login_required 
def bug_detail(request, pk):
    """
    bug pages
    """
    bug = get_object_or_404(Bug, pk=pk)
    bug.views += 1
    bug.save()
    comments = Comment.objects.filter(bug=bug).order_by('-created_date')
    # if request.method == 'POST':
    #     bug = Bug.objects.get(pk=pk)
    #     comment_form = CommentForm(request.POST)
    #     comment = request.POST.get('comment')
    #     # created_date = request.POST.get('created_date')
    #     if comment_form.is_valid():
    #         comment_group = comment_form.save(commit=False)
    #         comment_group.bug_id=pk
    #         comment_group.author_id=request.user.id
    #         comment_group=comment_form.save()
    context =  { 'bug':bug, 'comments' : comments}
    return render(request, "bugdetail.html", context)

@login_required
def bug_upvote(request, bug_id):
    """
    bug upvote
    """
    voter=request.user.id
    bugpk = Bug.objects.get(pk=bug_id)
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
def create_or_edit_bug(request, pk=None):
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