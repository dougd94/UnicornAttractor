from django import forms
from .models import Bug, Comments


class BugForm(forms.ModelForm):

    class Meta:
        model = Bug
        fields = ('name', 'description')
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('comment', 'created_date')
        