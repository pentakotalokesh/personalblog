from .models import comments
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model=comments
        fields = ('name','body')

