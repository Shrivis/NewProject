import cv2
import random
import string
import time
import time
from cv2 import threshold
# from tensorflow.keras.preprocessing.image import img_to_array
import os
import numpy as np
from tensorflow.keras.models import model_from_json

# Load Face Detection Model
face_cascade = cv2.CascadeClassifier("./temp/models/haarcascade_frontalface_default.xml")
# Load Anti-Spoofing Model graph
json_file = open('./temp/liveness_detector/liveness_model.json','r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
# load antispoofing model weights 
model.load_weights('./temp/liveness_detector/liveness_model.h5')


video = cv2.VideoCapture(0)
tests = []
delay=5
threshold=time.time()+delay
for i in range(10):
    try:
        ret,frame = video.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:  
            face = frame[y-5:y+h+5,x-5:x+w+5]
            resized_face = cv2.resize(face,(160,160))
            resized_face = resized_face.astype("float") / 255.0
            resized_face = np.expand_dims(resized_face, axis=0)
            # pass the face ROI through the trained liveness detector
            # model to determine if the face is "real" or "fake"
            preds = model.predict(resized_face)[0]
            tests += [preds[0]]
            # if preds> 0.3:
            #     label = 'Fake'
            #     cv2.putText(frame, label, (x,y - 10),
            #         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
            #     cv2.rectangle(frame, (x, y), (x+w,y+h),
            #         (0, 0, 255), 2)
            # else:
            #     label = 'Real'
            #     cv2.putText(frame, label, (x,y - 10),
            #         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
            #     cv2.rectangle(frame, (x, y), (x+w,y+h),
            #     (0, 255, 0), 2)
        cv2.imshow('frame', frame)

        letters = string.ascii_lowercase
        res = ''.join(random.choice(letters) for i in range(10))
        path = f'./real/image{i}.jpg'
        # _, image = video.read()
        print('********\nSaving\n')
        cv2.imwrite(path, resized_face)
        # cv2.imwrite(path, resized_face)
    except Exception as e:
        pass
video.release()        
cv2.destroyAllWindows()