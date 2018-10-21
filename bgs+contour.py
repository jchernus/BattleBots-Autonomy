import numpy as np
import cv2
import sys
import imutils

cap = cv2.VideoCapture("test-videos/battle_2018-04-14-19-20-08.mp4")

#Just here for Windows
#cv2.ocl.setUseOpenCL(False)

fgbg = cv2.createBackgroundSubtractorMOG2()

while (cap.isOpened):
    
    #if ret is true than no error with cap.isOpened
    ret, frame = cap.read()
    if ret==True:
        #apply background substraction
        fgmask = fgbg.apply(frame)

        # find contours
        (im2, contours, hierarchy) = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        #looping for contours
        for c in contours:
            if cv2.contourArea(c) < 500:
                continue

            #get bounding box from countour
            (x, y, w, h) = cv2.boundingRect(c)

            #draw bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Create and resize windows
        cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
        #cv2.namedWindow('fgmask',cv2.WINDOW_NORMAL)
        
        frame = imutils.resize(frame, width=500)
        (H, W) = frame.shape[:2]
        cv2.resizeWindow('fgmask',500,500)

        cv2.imshow('frame',frame)
        #cv2.imshow('fgmask',fgmask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

