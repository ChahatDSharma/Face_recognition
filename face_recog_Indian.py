# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 20:59:36 2021

@author: COSMIC和平DEVIL
"""
import os
import face_recognition
import shutil
#change the below path with path of your folder of all images
images = os.listdir(r'C:\Users\Purvak Sharma\Desktop\verzeo project\humans')
for image in images:
    try:
        img1=face_recognition.load_image_file("humans/" + image)
        lst1=list(face_recognition.face_encodings(img1)[0])
        a=lst1[1]
        b=lst1[2]
        c=lst1[8]
        d=lst1[10]
        e=lst1[15]
        xdmn,xdmx=0.0066780784875154495,0.18018855834007263
        cdmn,cdmx= 0.003818758297711611,0.12235910856723785
        ghmn,ghmx=0.08249840885400772,0.291446328163147
        yzmn,yzmx=0.05185400152206421,0.23117467761039734
        pqmn,pqmx=0.006780214607715607,0.21430179274082184
        if (a>xdmn and a<xdmx) and (b>cdmn and b<cdmx) and (c>ghmn and c<ghmx) and (d>yzmn and d<yzmx) and (e>pqmn and e<pqmx):
            print("\ngiven image is an indian adult!: " + image)
            files = [r'C:\Users\Purvak Sharma\Desktop\verzeo project\humans''\\' + image]
            for f in files:
                shutil.move(f, 'Indian_Origin')
        else:
             print("\nnot indian adult: " + image)

        #min and max ranges of HAAR features of Indians 
        abmn,abmx= -0.08488436043262482,0.08697349578142166
        rsmn,rsmx= -0.1180361658334732,0.06882413476705551
        tumn,tumx= 0.14881911873817444,0.25034090876579285
        vwmn,vwmx=0.19123037159442902,0.30428987741470337
        mnmn,mnmx= 0.12825259566307068,0.22264719009399414

        if (a>abmn and a<abmx) and (b>rsmn and b<rsmx) and (c>tumn and c<tumx) and (d>vwmn and d<vwmx) and (e>mnmn and e<mnmx):
            print("\ngiven image is an indian kid!: " + image)
            files = [r'C:\Users\Purvak Sharma\Desktop\verzeo project\humans''\\' + image]
            for f in files:
                shutil.move(f, 'Indian Origin')   
        else:
            print("\nnot indian kid: " + image)

    except:
        pass



    
 



