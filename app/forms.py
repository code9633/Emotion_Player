from django import forms
from app.model import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control form-control-sm mb-3'
    }))
    
    email = forms.CharField(widget=forms.TextInput(attrs= {
        'class' : 'form-control form-control-sm mb-3'
    }))
    
    password1 = forms.CharField(widget= forms.PasswordInput(attrs = {
        'class' : 'form-control form-control-sm mb-3'
    }))
    
    password2 = forms.CharField(widget= forms.PasswordInput(attrs ={
        'class' : 'form-control form-control-sm mb-5'
    }))
    
    class Meta :
        model = User
        fields = ['username', 'email', 'password1', 'password2']