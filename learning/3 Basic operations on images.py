import numpy as np
import cv2 as cv
import sys

e1 = cv.getTickCount()

img = cv.imread("learning/StarryNight.jpeg")
if img is None:
    sys.exit("Could not read the image.")

e2 = cv.getTickCount()
time = (e2 - e1)/ cv.getTickFrequency()
print(time) # time taken to read the image is 0.0066s

px = img[100,100] 

# experiment: try to make every other pixel white 
for x in range(0,160,2): # x = height 
    for y in range(0,310,2): # y = width
        img[x,y] = [255,255,255] # modifies RGB value 

cv.imshow("Display window", img)


k = cv.waitKey(0) # displayed until the user presses a key; 0 means to wait forever; counted in milliseconds 

if k == ord("s"): 
    cv.imwrite("learning/StarryNight.jpeg", img)
