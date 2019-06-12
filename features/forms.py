from django import forms
from .models import Feature, Commentf

class FeatureForm(forms.ModelForm):

    class Meta:
        model = Feature
        fields = ('name', 'description')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentf
        fields = ('content',)
        
