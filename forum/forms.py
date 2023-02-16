from django import forms
from .models import ForumPost

class NewPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = {"body","image"}