import cv2
import numpy as np

img = cv2.imread("messi5.jpg")
img2 = cv2.imread("opencv-logo.png")

print(img.shape)
print(img.size)
print(img.dtype)

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

#newImg = cv2.add(img, img2)
newImg = cv2.addWeighted(img, 0.5, img2, 0.5, 0)

cv2.imshow("window", img)
cv2.imshow("window2", newImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
