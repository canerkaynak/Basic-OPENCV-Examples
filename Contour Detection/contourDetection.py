import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread("logo.jpg")
bg = np.ones((820, 1236, 3), np.uint8)
imgray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
rgbimg = cv.cvtColor(img, cv.COLOR_BGR2RGB)

_, threshed = cv.threshold(imgray, 110, 255, 0)

contours, hierarchy = cv.findContours(threshed,
                                       cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cv.drawContours(img, contours, -1, (0, 0, 255), 2)
cv.drawContours(bg, contours, -1, (0, 0, 255), 2)
contouredImg = cv.cvtColor(img, cv.COLOR_BGR2RGB)
contouredBg = cv.cvtColor(bg, cv.COLOR_BGR2RGB)

titles = ["image", "contours", "contoured"]
images = [rgbimg, contouredBg, contouredImg]


for i in range(3):
    plt.subplot(1, 3, i+1), plt.imshow(images[i])
    plt.title(titles[i])

plt.show()
