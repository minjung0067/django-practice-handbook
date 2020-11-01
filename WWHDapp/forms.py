from django import forms
from .models import Post

class createForm(forms.Form):
    pic = forms.ImageField(label="photo")

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['brand','text','title','pic','category']    