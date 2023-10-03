from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import cv2
import base64
import numpy as np
import tensorflow as tf

from app.forms import UserForm

model = tf.keras.models.load_model('./files/model/final_model_V3.h5')

# Create your views here.

def home(request):
    return HttpResponse("This is the login Page")

# def predict_emotion(request):
    
#     print(request.POST)
    
#     if request.method == 'POST':
        
#         # get the image data  from the POST request as a Base64-encoded string
#         image_data = request.POST.get('image', None)
        
#         if image_data :
#             #decode the Base64  image data to byte
#             image_byte = base64.b64decode(image_data)
            
#             #create a Numpy array from the bytes
#             image_np = np.frombuffer(image_byte, np.uint8)
            
#             image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

#             # convert the image in to gray image
#             faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 
#                                                 'files/cascade_file/haarcascade_frontalface_default.xml')
#             gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
#             faces = faceCascade.detectMultiScale(gray, 1.1, 4)
#             for x,y,w,h in faces:
#                 roi_gray = gray[y:y+h, x:x+w]
#                 roi_color = image[y:y+h, x:x+w]
#                 cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0,0), 2) #BGR
#                 faces = faceCascade.detectMultiScale(roi_gray)
#                 if len(faces) == 0:
#                     print("Face not detected")
#                 else:
#                     for (ex,ey, ew, eh) in faces:
#                         face_roi = roi_color[ey: ey+eh, ex: ex+ew]
        
    
#             final_image = cv2.resize(face_roi, (48,48))
#             final_image = np.expand_dims(final_image, axis=0)
#             final_image = final_image/255.0
            
#             #load the model
            
#             
            
#             predict_emotion = model.predict(final_image)
#             int_prediction = np.argmax(predict_emotion)
            
#             labels = {'0' : 'Angry', '1':'Happy', '2': 'sad', '3' : 'Neutral'}
    
#             prediction = labels[int_prediction]
            
#             return redirect('result', prediction = prediction)
        
#         else :
#             return JsonResponse({'error' : 'Invalid image data'})
#     else:
#         return JsonResponse({'error': 'Invalid request'})  
    
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
            
            print(image.shape)
            
            faceCascade =  cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            faces = faceCascade.detectMultiScale(gray, 1.1, 4)
            for x,y,w,h in faces:
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = image[y:y+h, x:x+w]
                cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0,0), 2) #BGR
                faces = faceCascade.detectMultiScale(roi_gray)
                if len(faces) == 0:
                    print("Face not detected")
                else:
                    for (ex,ey, ew, eh) in faces:
                        face_roi = roi_color[ey: ey+eh, ex: ex+ew]
        
    
            final_image = cv2.resize(face_roi, (48,48))
            final_image = np.expand_dims(final_image, axis=0)
            final_image = final_image/255.0
               
            
            predict_emotion = model.predict(final_image)
            int_prediction = np.argmax(predict_emotion)
            
            print(int_prediction)
            
            labels = {0 : 'Angry', 1 :'Happy', 2 : 'sad', 3 : 'Neutral'}
    
            emotion = labels[int_prediction]
            


            return render(request, 'app/result.html', {'emotion': emotion})

    return render(request, 'app/predict_emotion.html')




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
