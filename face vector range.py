# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 20:59:36 2021

@author: COSMIC和平DEVIL
"""


import face_recognition
import os
images = os.listdir(r'C:\Users\Purvak Sharma\Desktop\chahat\Face Recog PROjeKt')
for image in images:
    img1= face_recognition.load_image_file('bb.png')
    lst1= list(face_recognition.face_encodings(img1)[0])
    print("face landmark array of the image is : ", lst1)
    a=lst1[1]
    b=lst1[2]
    c=lst1[8]
    d=lst1[10]
    e=lst1[15]
    print("")
    print("specific vector of a feature:",a)
    print("specific vector of a feature 2:",b)
    print("specific vector of a feature 3:",c)
    print("specific vector of a feature 4:",d)
    print("specific vector of a feature 5:",e)
