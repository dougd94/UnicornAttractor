from django import forms
from .models import Bug, Comment


class BugForm(forms.ModelForm):

    class Meta:
        model = Bug
        fields = ('name', 'description')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        
