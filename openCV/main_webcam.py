# DAVIDRVU - 2019

# pip install opencv-python

import cv2
import os
# initialize the camera
cam    = cv2.VideoCapture(0)   # 0 -> index of camera

#print(cam.get(412))
#print(cam.get(411))
#
#asd = cam.set(412,0)
#
#print(asd)
#
#print(cam.get(412))
#cam.set(cv2.CAP_PROP_SETTINGS,0) # 1
#print(cam.get(cv2.CAP_PROP_SETTINGS))
##cam.set(cv2.CV_CAP_PROP_BACKLIGHT, 0)

s, img = cam.read()
if s:    # frame captured without any errors
    cv2.imwrite(str(os.environ.get('USERPROFILE')) + "/Desktop/photo.jpg",img) #save image

print("DONE!")