import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread("saltAndPepperNoise.png")

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)


kernel = np.ones((5, 5), np.float32)/25
filtered = cv.filter2D(img, -1, kernel)

blur = cv.blur(img, (5, 5))

gaussian = cv.GaussianBlur(img, (5, 5), 0)

median = cv.medianBlur(img, 5)

bilateralF = cv.bilateralFilter(img , 9, 75, 75)

titles = ["image", "filtered", "blur", "gaussian blur", "median",
          "bilateral filter"]
images = [img, filtered, blur, gaussian, median, bilateralF]


for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i])
    plt.title(titles[i])

plt.show()
