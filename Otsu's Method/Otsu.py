import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread("logo.jpg", 0)

high_thresh, thresh_im = cv.threshold(img, 0, 255, cv.THRESH_BINARY +
                                       cv.THRESH_OTSU)
lowThresh = 0.5*high_thresh

print("Low Thresh: ", lowThresh, "-High Thresh: ", high_thresh)
