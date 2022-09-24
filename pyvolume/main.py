import cv2 
import mediapipe as mp
from math import hypot
import numpy as np

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
wCam, hCam = 640, 480 #Dimensiones webcam
cap.set(3,wCam)
cap.set(4,hCam)

mpHands = mp.solutions.hands 
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

volMin,volMax = volume.GetVolumeRange()[:2]

while True:
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    lmList = []
    #Dibuja landmark
    if results.multi_hand_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            for id,lm in enumerate(handlandmark.landmark):
                h,w,_ = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy]) 
            mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS)
    
    if lmList != []:
        #Dedos a detectar 4 y 8
        x1,y1 = lmList[4][1],lmList[4][2]
        x2,y2 = lmList[8][1],lmList[8][2]
        cx,cy = (x1+x2)//2, (y1+y2)//2

        #Dibujando los circulos distintivos
        cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
        cv2.circle(img,(x2,y2),15,(255,0,255),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 13), cv2.FILLED)

        length = hypot(x2-x1,y2-y1) #Determina el range entre mis dedos
        
        if length < 30:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

        vol = np.interp(length,[25,300],[volMin,volMax])
        print(vol,length)

        #print(volMin,volMax)
        volume.SetMasterVolumeLevel(vol, None)

        # Hand range 25 - 300
        # Volume range -65.25 - 0.0
        
    cv2.imshow('Volume Control v0.1 - UAPA',img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break