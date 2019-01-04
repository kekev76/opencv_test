import numpy as np
import cv2

videoFilePath = "files/babyfoot.mp4"

captureVideo = cv2.VideoCapture(videoFilePath)

while (captureVideo.isOpened()):
    ret, frame = captureVideo.read()

    # Convert image
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frameGray', grayImage)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captureVideo.release()
cv2.destroyAllWindows()