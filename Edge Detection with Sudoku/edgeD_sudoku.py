import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread("sudoku.png")
imgray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

laplacian = cv.Laplacian(imgray, cv.CV_64F, ksize = 3)
laplacian = np.uint8(np.absolute(laplacian))

sobelX = cv.Sobel(imgray, cv.CV_64F, 1, 0, ksize = 3)
sobelX = np.uint8(np.absolute(sobelX))

sobelY = cv.Sobel(imgray, cv.CV_64F, 0, 1, ksize = 3)
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv.bitwise_or(sobelX, sobelY)

canny = cv.Canny(img, 40, 96)


titles = ["image", "laplacian", "sobel x", "sobel y",
          "sobelCombined", "canny"]
images = [img, laplacian, sobelX, sobelY, sobelCombined, canny]


for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])

plt.show()
