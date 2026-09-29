import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1) # the laptop camera detects blue objects

while True:

    # Take each frame
    _, frame = cap.read()
    frame = cv.flip(frame, 1)

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # cv.COLOR_BGR2HSV convert image's color from RGB to gray (color spaces) -> extract object

    # define range of blue color in HSV - hue, saturation, value
    lower_blue = np.array([110,50,30])
    upper_blue = np.array([130,255,120]) 
    # observation: the blue needs to be under light to be detected well 

    # experiment with green and red 
    lower_green = np.array([110,40,30])
    upper_green = np.array([130,110,120]) 

    lower_red = np.array([0,90,30])
    upper_red = np.array([30,110,120]) 
    
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv.inRange(hsv, lower_green, upper_green)
    mask3 = cv.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    mask_all = mask | mask2 | mask3
    res = cv.bitwise_and(frame,frame, mask=mask_all) 
    # bitwise_or = keep a pixel if it is color A or B 

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == ord("q"): 
        break

cv.destroyAllWindows()