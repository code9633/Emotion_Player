from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import cv2
import base64
import numpy as np
import tensorflow as tf

from app.forms import UserForm
from .model import Song

model = tf.keras.models.load_model('./models/final_model_V3.h5')

# Create your views here.

def home(request):
    
    emotion = request.session.get('e')
    return render(request, "homepage/homepage.html")


def predict_emotion(request):
    
    if request.method == 'POST':
        captured_image_base64 = request.POST.get('captured_image', '')
        if captured_image_base64:
            # Decode the base64 image data
            captured_image_data = base64.b64decode(captured_image_base64.split(',')[1])

            # Convert the image data to a numpy array
            nparr = np.frombuffer(captured_image_data, np.uint8)

            # Decode the image using OpenCV
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # convert the image in to gray image
            faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            faces = faceCascade.detectMultiScale(gray, 1.1, 4)
            
            # Initialize face_roi outside the loop
            face_roi = None
            
            for x, y, w, h in faces:
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = image[y:y+h, x:x+w]
                cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)  # BGR
                faces = faceCascade.detectMultiScale(roi_gray)
                if len(faces) == 0:
                    print("Face not detected")
                else:
                    for (ex, ey, ew, eh) in faces:
                        face_roi = roi_color[ey:ey+eh, ex:ex+ew]
            
            if face_roi is not None:
                final_image = cv2.resize(face_roi, (48, 48))
                final_image = np.expand_dims(final_image, axis=0)
                final_image = final_image / 255.0

                predict_emotion = model.predict(final_image)
                int_prediction = np.argmax(predict_emotion)

                # labels = {0: 'Angry', 1: 'Happy', 2: 'Sad', 3: 'Neutral'}

                # emotion = labels[int_prediction]
                
                request.session['emotion'] = int_prediction
                
                return render(request, 'homepage/homepage.html')
            else:
                return JsonResponse({'error': 'Face not detected'})

    return render(request, 'predict_emotion.html')


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
