# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 20:59:36 2021

@author: COSMIC和平DEVIL
"""
import os
import face_recognition
import shutil
#change the below path with path of your folder of all images
images = os.listdir(r'C:\Users\Purvak Sharma\Desktop\verzeo project\All Images')
for image in images:
    try:
        img1=face_recognition.load_image_file("All Images/" + image)
        lst1=list(face_recognition.face_encodings(img1)[0])
        print("human face detected in : ", image)
        #change the below path with path of your folder of all images
        files = [r'C:\Users\Purvak Sharma\Desktop\verzeo project\All Images''\\' + image]
        for f in files:
            shutil.move(f, 'humans')
            
   
    except:
        print("\nnot human or face not detected in : " , image)
#change the below path with path of your folder of all images
        files = [r'C:\Users\Purvak Sharma\Desktop\verzeo project\All Images''\\' + image]
        for f in files:
            shutil.move(f, 'not humans')
        pass
 


    
 



