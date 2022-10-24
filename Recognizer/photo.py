import cv2
import time
import time
import string 
import random
import os
from cv2 import imshow
import numpy as np
from PIL import Image
print(os.getcwd())
path1 = './spoof/'
path2 = './spoofd/' 
face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

listing = os.listdir(path1)    
for file in listing:
    # frame = Image.open(path1 + file)   
    gray = cv2.imread(path1+file, cv2.COLOR_BGR2GRAY)
    frame = gray
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:  
        face = frame[y-5:y+h+5,x-5:x+w+5]
        resized_face = cv2.resize(face,(160,160))
        # imshow('face',face)
        cv2.imwrite(path2+file, face)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break      
        # resized_face = resized_face.astype("float") / 255.0
        # resized_face = img_to_array(resized_face)
        # resized_face = np.expand_dims(resized_face, axis=0)
        # pass the face ROI through the trained liveness detector
        # model to determine if the face is "real" or "fake"
'''
    cv2.imshow('frame', frame)

        preds = model.predict(resized_face)[0]
        print(preds)
        if preds> 0.5:
            label = 'spoof'
            cv2.putText(frame, label, (x,y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
            cv2.rectangle(frame, (x, y), (x+w,y+h),
                (0, 0, 255), 2)
        else:
            label = 'real'
            cv2.putText(frame, label, (x,y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
            cv2.rectangle(frame, (x, y), (x+w,y+h),
            (0, 255, 0), 2)
'''