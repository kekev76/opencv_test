import cv2
import numpy as np
import matplotlib.pyplot as plt

capture = cv2.VideoCapture("babyfoot.mp4")


fig, ax = plt.subplots()

ax.set_title("Histogram")
ax.set_xlabel('Bin')
ax.set_ylabel('Frequency')

lw = 3
alpha = 0.5

lineR, = ax.plot(np.arange(16), np.zeros((16,)), c='r', lw = lw)
lineG, = ax.plot(np.arange(16), np.zeros((16,)), c='g', lw = lw)
lineB, = ax.plot(np.arange(16), np.zeros((16,)), c='b', lw = lw)

ax.set_xlim(0, 255)
ax.set_ylim(0, 1)

plt.ion()
plt.show()


while (capture.isOpened()):
    ret, frame = capture.read();

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    numPixels = np.prod(frame.shape[:2])

    (b,g,r) = cv2.split(frame)

    histR = cv2.calcHist([r], [0], None, [256], [0, 255]) /numPixels
    histG = cv2.calcHist([g], [0], None, [256], [0, 255]) /numPixels
    histB = cv2.calcHist([b], [0], None, [256], [0, 255]) /numPixels

    lineR.set_ydata(histR)
    lineG.set_ydata(histG)
    lineB.set_ydata(histB)

    fig.canvas.draw()

    blur = cv2.GaussianBlur(gray, (11,11),0)

    (ret1,result) = cv2.threshold(blur, 160,255,cv2.THRESH_BINARY)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()