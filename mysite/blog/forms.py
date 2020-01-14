from django import forms
from .models import Comment

# forms est un module
# Form and ModelForm are classes of the forms module
# EmailPostForm are subclasses of Form or ModelForm classes

class EmailPostForm(forms.Form):
       name = forms.CharField(max_length=25)
       email = forms.EmailField()
       to = forms.EmailField()
       comments = forms.CharField(required=False,widget=forms.Textarea)


class CommentForm(forms.ModelForm):
   class Meta:
       model = Comment
       fields = ('name', 'email', 'body')

class SearchForm(forms.Form):
   query = forms.CharField()
