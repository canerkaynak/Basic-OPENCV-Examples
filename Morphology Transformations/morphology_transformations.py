import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread("smarties.png", 0)

#img = cv.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, masked = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernal = np.ones((5, 5), np.uint8)
dilation = cv.dilate(masked, kernal, 2)

kernal2 = np.ones((2, 2), np.uint8)
erosionWdilation = cv.erode(dilation, kernal2, 2)

opening = cv.morphologyEx(masked, cv.MORPH_OPEN, kernal)

closing = cv.morphologyEx(masked, cv.MORPH_CLOSE, kernal)

gradient = cv.morphologyEx(masked, cv.MORPH_GRADIENT, kernal)

topHat = cv.morphologyEx(masked, cv.MORPH_TOPHAT, kernal)

titles = ["image", "masked", "dilation",
          "erosion after dilation", "opening", "closing",
          "gradient", "topHat"]
images = [img, masked, dilation, erosionWdilation, opening,
          closing, gradient, topHat]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])

plt.show()
