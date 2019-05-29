from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Bug
from .forms import BugForm


# Create your views here.
# show all bugs
def all_bugs(request):
    bugs = Bug.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "bugs.html", {"bugs": bugs})
    
def bug_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    bug = get_object_or_404(Bug, pk=pk)
    bug.views += 1
    bug.save()
    return render(request, "postdetail.html", {'bug': bug})
    
def create_or_edit_bug(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if request.method == "POST":
        form = BugForm(request.POST, request.FILES, instance=bug)
        if form.is_valid():
            bug = form.save()
            return redirect(bug_detail, bug.pk)
    else:
        form = BugForm(instance=bug)
    return render(request, 'bugform.html', {'form': form})