from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms 

from .models import ImageModel

class RegisterForm(UserCreationForm):

    password1 = forms.CharField()
    password2 = forms.CharField()
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']


class LoginForm(AuthenticationForm):
    username = forms.CharField( label='Enter Your UserName')
    password = forms.CharField(label='Enter Your Password')

    class Meta:
        model = User
        fields = User
        fields = ['username', 'password']


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['title','cat','image','desc']

        labels = {
            'title':'Enter Your Title',
            'cat':'Enter Your Categories',
            'image':'Enter Your Image',
            'desc':'Enter Your Description'

        }