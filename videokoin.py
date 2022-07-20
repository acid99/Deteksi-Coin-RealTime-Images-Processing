#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 11:38:34 2022

@author: littlepig
"""

import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
        print("Tidak bisa Membuka Kamera")
        exit()

#input kamera ke frame
while True:
        #capture 
        ret, frame = cap.read()
        frame = cv.resize(frame, (400, 400), fx = 0, fy = 0, interpolation = cv.INTER_CUBIC)
        
        #jika frame dapat dibaca ret true
        if not ret:
                print("Tidak dapat menangkap frame...")
                break
            
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        blur = cv.GaussianBlur(gray, (11,11), 0)

        canny = cv.Canny(blur, 30, 150, 3)

        dilated = cv.dilate(canny, (1,1), iterations = 2)

        (cnt, heirarchy) = cv.findContours(dilated.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        cv.drawContours(rgb, cnt, -1, (0,255,0), 2)

        Teks = "Jumlah koin pada video = {}".format(len(cnt))
        font = cv.FONT_HERSHEY_PLAIN

        cv.putText(rgb, Teks, (10,20), font, 1.5, (0,0,255),  1, cv.LINE_AA)
        
        #display
        
        cv.imshow('Deteksi Koin', rgb)
        cv.imshow('Asli', frame)
        
        if cv.waitKey(1) == ord('q'):
            break

cap.release()
cv.waitKey(0);
cv.destroyAllWindows();