import cv2
import numpy as np


def crop():

    if points[0][1] < points[1][1] and points[0][0] < points[1][0]:
        croped = img[points[0][1]:points[1][1], points[0][0]:points[1][0]]
    elif points[0][1] > points[
        1][1] and points[0][0] < points[1][0]:
        croped = img[points[1][1]:points[0][1], points[0][0]:points[1][0]]
    elif points[0][1] > points[1][1] and points[0][0] > points[1][0]:
        croped = img[points[1][1]:points[0][1], points[1][0]:points[0][0]]
    else:
        croped = img[points[0][1]:points[1][1], points[1][0]:points[0][0]]

    points.clear()
    return croped

def pointAdd(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])

img = cv2.imread("children.jpg")

cv2.putText(img, "To Exit Press 'ESC'",
                   (10, 1600), cv2.FONT_HERSHEY_DUPLEX , 2, (0, 0, 0), 2)
cv2.putText(img, "To Crop Click To Two Points",
                   (10, 1680), cv2.FONT_HERSHEY_DUPLEX , 2, (0, 0, 0), 2)
cv2.namedWindow("Window")

width = int(img.shape[1] * 0.4)
height = int(img.shape[0] * 0.4)

img = cv2.resize(img, (width, height))

points = []

cv2.setMouseCallback("Window", pointAdd)

while True:
    cv2.imshow("Window", img)
    if len(points) == 2:
        croped = crop()
        cv2.imshow("Cropped",croped)
    
    k = cv2.waitKey(1)
    if k == 27 & 0xFF:
        break
cv2.destroyAllWindows()
