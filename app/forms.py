from django import forms
from app.model import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control my-2'
    }))
    
    email = forms.CharField(widget=forms.TextInput(attrs= {
        'class' : 'form-control my-2'
    }))
    
    password1 = forms.CharField(widget= forms.PasswordInput(attrs = {
        'class' : 'form-control my-2'
    }))
    
    password2 = forms.CharField(widget= forms.PasswordInput(attrs ={
        'class' : 'form-control my-2'
    }))
    
    class Meta :
        model = User
        fields = ['username', 'email', 'password1', 'password2']