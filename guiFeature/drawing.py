import numpy as np
import cv2

# Create black image
image = np.zeros((512,512,3), np.uint8)

#Create line whith thickness of 5 px
image = cv2.line(image, (0,0), (511,511), (255,0,0), 5)

#Create rectangle
image = cv2.rectangle(image, (384,0), (510,128), (0,255,0), 3)

#Create circle
image = cv2.circle(image, (447,63), 63, (0,0,255), -1)

#Create Ellipse
image = cv2.ellipse(image, (256,256), (100,50), 0,0,180,255,-1)

#Create polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
image = cv2.polylines(image, [pts], True, (0,255,255))

#Create Text
font = cv2.FONT_HERSHEY_SIMPLEX
image = cv2.putText(image, "OpenCV", (10,500), font, 0.4, (255,255,255),1,cv2.LINE_AA)


#show image
cv2.imshow("result",image)
cv2.waitKey(0)
cv2.destroyAllWindows()