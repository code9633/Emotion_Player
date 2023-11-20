from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    
    username = forms.CharField(widget= forms.TextInput(attrs={
        "class" : "input",
        "placeholder" : "Username"
    }))
    
    email = forms.CharField(widget= forms.EmailInput(attrs={
        "class" : "input",
        "placeholder" : "Email"
    }))
    
    password1 = forms.CharField(widget= forms.PasswordInput(attrs={
        "class" : "input",
        "placeholder" : "Password"
    }))
    
    password2 = forms.CharField(widget= forms.PasswordInput(attrs={
        "class" : "input",
        "placeholder" : "Confirm Password"
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
        

class UserLoginForm(AuthenticationForm):
    
    username = forms.CharField(widget= forms.TextInput(attrs={
        "class" : "input",
        "placeholder" : "Username"
    }))
    
    password = forms.CharField(widget= forms.PasswordInput(attrs={
        "class" : "input",
        "placeholder" : "Password"
    }))

    class Meta:
        model = User
        fields = ['username', 'password']

    
