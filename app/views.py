from django.shortcuts import render, redirect
from django.http import  JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


from app.forms import UserForm
from .imageEmotion import ImageEmotionAnalyzer
from .songList import SongListManager


def home(request):     
    return render(request, "homepage/homepage.html")

def predict_emotion(request):
    
    if request.method == 'POST':
        captured_image_base64 = request.POST.get('captured_image', '')
        # get emotion as a number
        getEmotion = ImageEmotionAnalyzer(captured_image_base64)  
        emotion = getEmotion.image2emotion()
        
        # if emtion is available
        if emotion is not None:  
            
            emotion = int(emotion)
            getContext = SongListManager(emotion)  
            context = getContext.createPlayList()
            
            
            return render(request, 'homepage/homepage.html', context)

        else:
            return JsonResponse({'error': 'Face not detected'})
            
    return render(request, 'prediction/predict_emotion.html')


########### User Authentication #########################3

def signupPage(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully!')
            messages.success(request, 'Login to Continue')
            return redirect('/login')
    
    return render(request, 'authentication/signupPage.html', {'form' : form})

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
        
    return render(request, 'authentication/loginPage.html')
        
    
        
def logout(request):
  
    if request.user.is_authenticate:
        logout(request)
        messages.success(request, "Logged out Succesfully..")
