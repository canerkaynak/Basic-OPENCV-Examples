import cv2
import numpy as np

def value(x):
    pass



img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow("Window")

cv2.createTrackbar("B", "Window", 0, 255, value)
cv2.createTrackbar("G", "Window", 0, 255, value)
cv2.createTrackbar("R", "Window", 0, 255, value)

while True:
    cv2.imshow("Window", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv2.getTrackbarPos("B", "Window")
    g = cv2.getTrackbarPos("G", "Window")
    r = cv2.getTrackbarPos("R", "Window")

    img[:] = [b, g, r]

cv2.destroyAllWindows()
