import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

import cv2

import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/trashcan/Documents/google_cred.json"
# Imports the Google Cloud client library
from google.cloud import vision

camera = cv2.VideoCapture(0)



# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('/home/kahlawy/Projects/hackathon/final_shot/93216165.jpg')
while True:
    # Loads the image into memory
    ret, image = camera.read()
    success, encoded_image = cv2.imencode('.jpg', image)
    cv2.imwrite('hello.jpg',image)
    if ret:
        content2 = encoded_image.tobytes()

        image = vision.Image(content=content2)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        print('Labels:')
        print(response)
        # for label in labels:
        #     print(label.description)
        descriptions = [label.description for label in labels]
        for description in descriptions:
            if "bottle" in description:
                p.ChangeDutyCycle(5)
                time.sleep(1)
                p.ChangeDutyCycle(20)
                time.sleep(10)  
                p.ChangeDutyCycle(5)
                time.sleep(1)  
                break

