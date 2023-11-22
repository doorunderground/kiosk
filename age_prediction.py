# Run on the PC(server)
## 2023.06 / AI Age Estimation Kiosk

import pymysql
import pandas as pd
import numpy as np
import os
import socket
import cv2
from tensorflow.keras.models import Model, Sequential, load_model
from tensorflow.keras.layers import BatchNormalization, Conv2D, MaxPool2D, Activation, Dropout, Lambda, Dense, Flatten, Input
import tensorflow as tf
import tensorflow.keras as keras
import math
import time
import argparse

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Connect to MySQL
db = pymysql.connect(host="localhost",
                    user="root", password="5531",
                    charset="utf8")
cursor = db.cursor()

# Select the database
cursor.execute('USE db2;')

# Load the pre-trained model
age_model = load_model('C:/Users/wlgk5/TEST/age_model_new.h5') # set your correct path  

# OpenCV for face detection
face_cascade = cv2.CascadeClassifier('C:/Users/wlgk5/TEST/haarcascade_frontalface_default.xml') # set your correct path

# Webcam capture
camera = cv2.VideoCapture(0)

image_size = 200

# List to store predicted ages
age_list = []

# Socket communication setup
HOST = '172.20.10.3'  # Enter the IP address of your PC
PORT = 8000

def activate_camera():
    global age_list
    while True:
        ret, frame = camera.read()
        faces = face_cascade.detectMultiScale(frame,scaleFactor=1.11, minNeighbors=8)

        age_ = []
    
        for (x,y,w,h) in faces:
            img = frame[y:y + h, x:x + w]
            img = cv2.resize(img,(image_size,image_size))
            age_predict = age_model.predict(np.array(img).reshape(-1,image_size,image_size,3))
            age_.append(age_predict)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,225,0),1)
            cv2.putText(frame,"Age:"+str(int(np.round(age_predict))),(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,w*0.005,(255,255,0),1)
            
            age_list.append(age_predict[0])
        
        
        # If the list contains 6 predicted ages, calculate the average and store it in the database
        if len(age_list) == 6:
            age_avg = np.mean(age_list)
            print("Average predicted age:", int(np.round(age_avg))) 
            cursor.execute("DELETE FROM age") # Delete existing values in the database  
            cursor.execute("INSERT INTO age(age) VALUES ({})".format(int(np.round(age_avg)))) # Store the age of a new user in the database
            age_list = [] # After saving, reset the list
            camera.release() # Close the camera
            cv2.destroyAllWindows() # Close the window
            break
        
        time.sleep(0.7) 

        # If there are faces detected Print the predicted age
        if frame is not None and frame.shape[0] > 0 and frame.shape[1] > 0:
            cv2.imshow("camera", frame)

        if len(age_) > 0:
            print("Predicted age:", age_)

        key = cv2.waitKey(10)
        if key == 27:
            camera.release()
            cv2.destroyAllWindows()
            break
    db.commit()
    db.close()
    
# Decode the received data from the clinet(RaspberryPi), and if the message is "COME", call the activate_camera() function to active the camera
# Then, send the received data back to the client
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    while True:
        print("Waiting for connection...")
        conn, addr = s.accept()
        print("Connected by", addr)

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                message = data.decode("utf-8")
                print("Received:", message)

                if message == "Come":
                    print("Activating camera...")
                    activate_camera()

                conn.sendall(data)