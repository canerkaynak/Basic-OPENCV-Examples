import cv2
import numpy as np

while True:
    img = cv2.imread("smarties.png")

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    low_blue = np.array([110, 50, 50])
    high_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv_img, low_blue, high_blue)
    masked = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Window", masked)

    k = cv2.waitKey(1)
    if k == 27 & 0xFF:
        break
cv2.destroyAllWindows()
