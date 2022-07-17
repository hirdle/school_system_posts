
from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'text', 'visible_all', 'visible_class', 'img']

        widgets = {
            'img': forms.FileInput(attrs={'class': 'form-control'}),
        }