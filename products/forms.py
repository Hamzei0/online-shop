from django import forms

from .models import CommentProduct

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentProduct
        fields = ['text','stars']
        
        