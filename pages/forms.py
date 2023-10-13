from .models import Comment, Comment2, Comment3
from django import forms
class CommentForm(forms.ModelForm):
    class Meta:
     model = Comment
     fields = ('content',)
class Comment2Form(forms.ModelForm):
    class Meta:
     model = Comment2
     fields = ('content',)

class Comment3Form(forms.ModelForm):
    class Meta:
     model = Comment3
     fields = ('content',)

