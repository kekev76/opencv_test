import numpy as np
import cv2

imageFilePath = "files/lena.jpg"

#Load a color image
imgColor = cv2.imread(imageFilePath, cv2.IMREAD_COLOR) #image with color

imgGray =  cv2.imread(imageFilePath, cv2.IMREAD_GRAYSCALE) #image in grascale mode

imgAlpha = cv2.imread(imageFilePath, cv2.IMREAD_UNCHANGED) #image including alpha channel

#display image

#firs argument is the name of the window

#quick way
cv2.imshow("imageColor",imgColor)

#otherWay (same result)
cv2.namedWindow("imageGray", cv2.WINDOW_AUTOSIZE)
cv2.imshow("imageGray", imgGray)

#other way with resize window
cv2.namedWindow("imageAlpha", cv2.WINDOW_NORMAL)
cv2.imshow("imageAlpha",imgAlpha)

#Wait for any key touch (the argument is the time it will wait, if 0 so it wait indefinitely)
cv2.waitKey(0)

#Destroy all the windows create
cv2.destroyAllWindows()