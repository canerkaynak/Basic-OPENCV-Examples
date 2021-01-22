import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


video = cv.VideoCapture("vtest.avi")

#fourcc = cv.VideoWriter_fourcc(*'XVID')
#out = cv.VideoWriter("outputRec.avi", fourcc, 150, (576, 768))

_, frame1 = video.read()
_, frame2 = video.read()
ret=True

while ret:
    difference = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(difference, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    _, threshed = cv.threshold(blurred, 20, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(threshed, None, 2)
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #cv.drawContours(frame1, contours, -1, (0, 0, 255), 2)
    
    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour)
        if cv.contourArea(contour) < 800:
            continue
        cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv.putText(frame1, "Status: {}".format("Movement"),
                   (20, 550), cv.FONT_HERSHEY_DUPLEX , 1, (0, 0, 0), 2)

    cv.imshow("Video", frame1)
    #out.write(frame1)
    frame1 = frame2
    ret, frame2 = video.read()

    if cv.waitKey(150) == 27:
        break

video.release()
#out.release()
cv.destroyAllWindows()
