import numpy as np
import cv2 as cv

cap = cv.VideoCapture(1) # camera 1 for me is the webcam 

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID') 
out = cv.VideoWriter("output.mp4", fourcc, 20.0, (640, 400))  # FPS 20.0; width x height: 640 x 400


# check if cap is initialized
if not cap.isOpened(): 
    print("Cannot open camera")
    exit()

# Capture live video frame-by-frame
while True:
    ret, frame = cap.read() # returns a boolean (ret = return )

    if not ret:
        print("Can't receive frame.")
        break
    
    frame = cv.flip(frame, 1)
    frame = cv.resize(frame, (640, 400)) 
   
    # write the flipped frame ==> save video 
    out.write(frame)

    # Display the resulting frame
    cv.imshow('frame', frame) 
    if cv.waitKey(1) == ord('q'):
         break
  

# Release the capture
cap.release()
out.release()
cv.destroyAllWindows()