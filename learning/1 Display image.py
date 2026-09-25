import cv2 as cv # OpenCV python library
import sys

img = cv.imread(cv.samples.findFile("learning/StarryNight.jpeg"))

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img) 
k = cv.waitKey(0) # displayed until the user presses a key; 0 means to wait forever; counted in milliseconds 

if k == ord("s"): 
    cv.imwrite("learning/StarryNight.jpeg", img)

