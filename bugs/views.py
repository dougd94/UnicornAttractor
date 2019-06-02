from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Bug, Comments, Votes
from .forms import BugForm, CommentForm


# Create your views here.
# show all bugs
def all_bugs(request):
    bugs = Bug.objects.filter(created_date__lte=timezone.now()
        ).order_by('-created_date')
    return render(request, "bugs.html", {"bugs": bugs})
    
def bug_detail(request, pk):
    """
    bug pages
    """
    bug = get_object_or_404(Bug, pk=pk)
    bug.views += 1
    bug.save()
    if request.method == 'POST':
        bug = Bug.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        comment = request.POST.get('comment')
        created_date = request.POST.get('created_date')
        if comment_form.is_valid():
            comment_group = comment_form.save(commit=False)
            comment_group.bugpk_id=pk
            comment_group.author_id=request.user.id
            comment_group=comment_form.save()
    return render(request, "bugdetail.html", {'bug': bug})
    
def bug_upvote(request):
    """
    bug upvote
    """
    if request.method == 'POST':
        voter=request.user.id
        bugpk = request.GET.get('bugpk')
        upvotes = Bug.objects.get(pk=bugpk)
        
         # check if the if already voted
        upvote = Votes.objects.filter(bugpk=bugpk, voter=voter)
        
        if not upvote:
            
            # save the vote to databaase
            upvote = Votes(bugpk_id = bugpk, voter_id = request.user.id)
            upvote.save()
        
            count = Votes.objects.filter(bugpk_id=bugpk).count()
            
        #   adds upvote to model
            # upvotes.upvotes = count
            upvotes.upvotes += 1
            upvotes.save()
            messages.success(request, "You have successfully upvoted!")
            return redirect(reverse('all_bugs'))
        else: 
            messages.error = (request, 'You have already upvoted!')
            return redirect(reverse('all_bugs'))
            
        
        
  
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
            return redirect(bug_detail, bug.pk)
    else:
        form = BugForm(instance=bug)
    return render(request, 'bugform.html', {'form': form})