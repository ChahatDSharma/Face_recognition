# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 20:01:54 2021

@author: COSMIC和平DEVIL
"""

import face_recognition
img1=face_recognition.load_image_file("image (10).jpg")
lst1=list(face_recognition.face_encodings(img1)[0])
a=lst1[1]
b=lst1[2]
c=lst1[8]
d=lst1[10]
e=lst1[15]
print("first vector:",a)
print("2:",b)
print("3:",c)
print("4:",d)
print("5:",e)
print("")
xdmn=0.0066780784875154495
xdmx=0.18018855834007263
cdmn= 0.003818758297711611
cdmx= 0.12235910856723785
ghmn=0.08249840885400772
ghmx=0.291446328163147
yzmn=0.05185400152206421
yzmx=0.23117467761039734
pqmn=0.006780214607715607
pqmx=0.21430179274082184
if a>xdmn and a<xdmx:
    if b>cdmn and b<cdmx:
        if c>ghmn and c<ghmx:
            if d>yzmn and d<yzmx:
                if e>pqmn and e<pqmx:
                     print("\ngiven image is an indian adult!: ")
                else:
                    print("\nnot indian adult: ")
            else:
                print("\nnot indian adult: ")
        else:
            print("\nnot indian adult: ")
    else:
        print("\nnot indian adult: ")
else:
     print("\nnot indian adult:" )


abmn= -0.08488436043262482
abmx= 0.08697349578142166
rsmn= -0.1180361658334732
rsmx= 0.06882413476705551
tumn= 0.14881911873817444
tumx= 0.25034090876579285
vwmn=0.19123037159442902
vwmx=0.30428987741470337
mnmn= 0.12825259566307068
mnmx= 0.22264719009399414
if a>abmn and a<abmx:
    if b>rsmn and b<rsmx:
        if c>tumn and c<tumx:
            if d>vwmn and d<vwmx:
                if e>mnmn and e<mnmx:
                    print("\ngiven image is an indian kid!: " )
                else:
                    print("\nnot indian kid: " )
            else:
                print("\nnot indian kid: " )
        else:
            print("\nnot indian kid: " )
    else:
        print("\nnot indian kid: " )
else:
    print("\nnot indian kid: " )

