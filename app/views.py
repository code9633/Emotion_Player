from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .forms import UserRegistrationForm, UserLoginForm
from app.detect import ImageEmotionAnalyzer
from app.models import Songs


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
                messages.success(request, 'Login successful')
                messages.info(request, "Show your face")
                return redirect('/')

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


@csrf_exempt
def expression(request):
    uri = json.loads(request.body).get("image_uri")
    print(uri)
    getEmotion = ImageEmotionAnalyzer(uri)
    expression = getEmotion.image2emotion()
    print(expression)
    return JsonResponse({"mood": expression})

def get_music_details(request):
    mood = request.GET.get('mood','')
    songs = Songs.objects.filter(emotion = mood).values(
        'id', 'songName', 'artist', 'coverImage', 'audioFile', 'duration'
    )
    return JsonResponse(list(songs), safe=False)

@login_required
def index (request):
    return render(request, "main.html")

def userLogout(request):
    logout(request)
    messages.success(request, "Logged out Succesfully")
    return redirect('login')

