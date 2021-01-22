import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    global mode, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        if mode == True:
            cv2.circle(img, (x, y), 1, bgr, -1)
            points.append((x,y))
            if len(points) == 2:
                cv2.line(img, points[-1], points[-2], bgr, 3)
                points.clear()
            
    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True and mode == False:
            cv2.circle(img, (x, y), 5, bgr, -1)
    if event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x, y), 5, bgr, -1)

    

def value(x):
    pass


drawing = False
mode = True
    
img = np.zeros((512, 812, 3), np.uint8)
img = cv2.bitwise_not(img)
cv2.putText(img, "To Exit Press 'ESC'",
                   (10, 450), cv2.FONT_HERSHEY_DUPLEX , 0.5, (0, 0, 0), 1)
cv2.putText(img, "To Switch Line Mode-Spray Mode Press 'm'",
                   (10, 475), cv2.FONT_HERSHEY_DUPLEX , 0.5, (0, 0, 0), 1)
cv2.putText(img, "For Line Mode Click To Two Points, For Spray Mode Hold Down",
                   (10, 500), cv2.FONT_HERSHEY_DUPLEX , 0.5, (0, 0, 0), 1)
cv2.namedWindow("Window")

cv2.createTrackbar("Blue", "Window", 0, 255, value)
cv2.createTrackbar("Green", "Window", 0, 255, value)
cv2.createTrackbar("Red", "Window", 0, 255, value)

points = []
bgr=(0,0,255)
cv2.setMouseCallback("Window", click_event)

cv2.imshow("Window", img)
    

while True:
    b = cv2.getTrackbarPos("Blue", "Window")
    g = cv2.getTrackbarPos("Green", "Window")
    r = cv2.getTrackbarPos("Red", "Window")
    bgr = (b, g, r)
        
    cv2.imshow("Window", img)
        
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == ord("m"):
        mode = not mode

    

        
cv2.destroyAllWindows()

