import cv2 as cv

img = cv.imread("sudoku.png", 0)

_, thresholded = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

thresholded2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                    cv.THRESH_BINARY, 3, 3)

thresholded3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv.THRESH_BINARY, 3, 2)

cv.imshow("Original", img)
cv.imshow("Thresholded_1", thresholded)
cv.imshow("Thresholded_2", thresholded2)
cv.imshow("Thresholded_3", thresholded3)

cv.waitKey(0)
cv.destroyAllWindows
