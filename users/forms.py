from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']

class ProfileUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwards):
        super(ProfileUpdateForm, self).__init__(*args, **kwards)
        # self.fields['img'].label = "Изображение профиля"
        
    class Meta:
        model = Profile
        fields = ['user_class_number', 'user_class_letter']
        # fields = ['user_class_number', 'user_class_letter', 'img']

        widgets = {
            'img': forms.FileInput(attrs={'class': 'form-control'}),
        }