import cv2
import mediapipe as mp

from mediapipe.tasks import python # this is the newest mediapipe version from Google Developer (landmarker)
from mediapipe.tasks.python import vision

import time # to create frames

cap = cv2.VideoCapture(1) # for me, webcam no. 0 is phone, webcam no. 1 is laptop
mpHands = mp.solutions.hands
hands = mpHands.Hands()
# in Hands():
    # static_image_mode: tracks still images instead of videos 
    # max_num_hands = 2
    # min_detection / tracking_confidence: min score for an object to be considered successfully tracked
    # if this is 100%, the frames would be constantly rechecked; default 50% 
 

# set up MediaPipe - code from ChatGPT - Check where from? 
base_options = python.BaseOptions(
    model_asset_path="models/hand_landmarker.task"
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=2
)

detector = vision.HandLandmarker.create_from_options(options)
"""
while True:
    success, img = cap.read()
    cv2.imshow("Image",img)
    cv2.waitKey(1)"""



