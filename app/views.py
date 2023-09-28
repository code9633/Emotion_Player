from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from app.forms import UserForm

# Create your views here.

def home(request):
    return HttpResponse("This is the login Page")

def signupPage(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully!')
            messages.success(request, 'Login to Continue')
            return redirect('/login')
    
    return render(request, 'app/signupPage.html', {'form' : form})

def loginPage(request):
    
    if request.method == "POST":
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = user_name, password = password)
        
        if user is not None :
            login(request, user)
            messages.success(request, "Logged in Succesfully")
            return redirect("/")
        else :
            messages.error(request, "Invalid Username and Passord")
            return redirect('/login')
        
    return render(request, 'app/loginPage.html')
        
    
        
def logout(request):
  
    if request.user.is_authenticate:
        logout(request)
        messages.success(request, "Logged out Succesfully..")
