from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import UserRegistrationForm, UserLoginForm
from .image2emotion import ImageEmotionAnalyzer 

def userRegistration(request):
    registrationForm = UserRegistrationForm()
    if request.method == 'POST':
        registrationForm = UserRegistrationForm(request.POST)

        if registrationForm.is_valid():
            try:
                registrationForm.save()
                messages.success(request, 'Registration successful. Welcome!')
                return redirect('login')

            except Exception as e:
                messages.error(request, 'Error during registration: ' + str(e))

    return render(request, 'register.html', {
        'registrationForm': registrationForm,
        'loginForm': UserLoginForm(),
    })


def userLogin(request):
    loginForm = UserLoginForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            try:
                login(request, user)
                messages.success(request, 'Login successful. Welcome back!')
                return redirect('camera')

            except Exception as e:
                messages.error(request, 'Error during login: ' + str(e))
        else:
            messages.error(request, "Invalid Username and Password")
            return render(request, 'login.html', {
                "error" : "Invalid Username and Password",
                'registrationForm': UserRegistrationForm(),
                'loginForm': loginForm,
                
            })

    return render(request, 'login.html', {
        'registrationForm': UserRegistrationForm(),
        'loginForm': loginForm,
    })


@login_required
def getEmotion(request):
    
    if request.method == 'POST':
        capturedImage = request.POST.get('captured_image', '')
        
        getEmotion = ImageEmotionAnalyzer(capturedImage)
        emotion = getEmotion.image2emotion()
        
        if emotion is not None:
            emotion = int(emotion)

            return render(request, 'home.html', {"emotion": emotion})

        else :
            return render(request, 'camera.html', {"error" : "Face not detected.."})
    
    return render(request, 'camera.html', {'error' : "Can't campture the image"})    
        

@login_required
def home(request):
    return render(request, "home.html")

def userLogout(request):
    logout(request)
    return redirect('login')

