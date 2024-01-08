import numpy as np
import cv2
import base64
import tensorflow as tf

model = tf.keras.models.load_model('./Utilities/CNNmodel/emotionClassifier.h5')

class ImageEmotionAnalyzer:
    
    def __init__(self, captured_image):
        self.captured_image = captured_image

    def image2emotion(self):
        
        emotionNumber = None
        
        if self.captured_image:
            
            captured_image_data = base64.b64decode(self.captured_image.split(',')[1])
            nparr = np.frombuffer(captured_image_data, np.uint8)

            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
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
                emotionNumber = np.argmax(predict_emotion)
                
        print("Emtion number is ", emotionNumber)
        label = { 0: "Angry", 1: "Happy", 2: "Sad", 3:"Neutral"}
        mood = label[int(emotionNumber)]
        
        return mood