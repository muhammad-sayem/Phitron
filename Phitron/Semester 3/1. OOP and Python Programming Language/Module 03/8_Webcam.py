import cv2

cam = cv2.VideoCapture()
while True:
    _, frame = cam.read()
    cv2.imshow('My Cam', frame)
    cv2.waitKey(1)
