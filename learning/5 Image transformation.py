import numpy as np
import cv2 as cv

img = cv.imread('StarryNight.jpeg')
assert img is not None, "file could not be read, check with os.path.exists()"

# change image's location
rows,cols,channels = img.shape # three variables, channels = color channels (BGR)

M = np.float32([[1,0,100],[0,1,50]]) # matrix of how to shift in the x, y directions
# matrix: 1, 0, 100 ==> x = 100
#         0, 1, 50  ==> y = 50 
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1) # matrix of rotation 
# matrix: [cos x  -sin x]
#         [sin x   cos x]        
import matplotlib.pyplot as plt
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
# Perspective Transformation: make parallel lines parallel (eg CamScanner)

dst = cv.warpAffine(img,M,(cols,rows))

cv.imshow("Display window", dst)


k = cv.waitKey(0)
