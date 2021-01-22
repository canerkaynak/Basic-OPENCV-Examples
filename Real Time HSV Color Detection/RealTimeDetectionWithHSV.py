import cv2

source = 0 #Video source

max_value = 255
max_value_h = 360//2

low_h = 0
low_s = 0
low_v = 0
high_h = max_value_h
high_s = max_value
high_v = max_value

cv2.namedWindow("Original")
cv2.namedWindow("Thresholded")

def low_h_func(val):
    global low_h, high_h
    low_h = val
    low_h = min(high_h - 1, low_h)
    cv2.setTrackbarPos("Low Hue", "Thresholded", low_h)

def low_s_func(val):
    global low_s, high_s
    low_s = val
    low_s = min(high_s - 1, low_s)
    cv2.setTrackbarPos("Low Saturation", "Thresholded", low_s)

def low_v_func(val):
    global low_v, high_v
    low_v = val
    low_v = min(high_v - 1, low_v)
    cv2.setTrackbarPos("Low Value", "Thresholded", low_v)

def high_h_func(val):
    global low_h, high_h
    high_h = val
    high_h = max(low_h + 1, high_h)
    cv2.setTrackbarPos("High Hue", "Thresholded", high_h)

def high_s_func(val):
    global low_s, high_s
    high_s = val
    high_s = max(low_s + 1, high_s)
    cv2.setTrackbarPos("High Saturation", "Thresholded", high_s)

def high_v_func(val):
    global low_v, high_v
    high_v = val
    high_v = max(low_v + 1, high_v)
    cv2.setTrackbarPos("High Value", "Thresholded", high_v)

cv2.createTrackbar("Low Hue", "Thresholded", low_h, max_value_h, low_h_func)
cv2.createTrackbar("Low Saturation", "Thresholded", low_s, max_value, low_s_func)
cv2.createTrackbar("Low Value", "Thresholded", low_v, max_value, low_v_func)
cv2.createTrackbar("High Hue", "Thresholded", high_h, max_value_h, high_h_func)
cv2.createTrackbar("High Saturation", "Thresholded", high_s, max_value, high_s_func)
cv2.createTrackbar("High Value", "Thresholded", high_v, max_value, high_v_func)

video = cv2.VideoCapture(source)

while True:
    ret, frame = video.read()

    if frame is None:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    thresholded = cv2.inRange(hsv, (low_h, low_s, low_v), (high_h, high_s, high_v))

    cv2.imshow("Original", frame)
    cv2.imshow("Thresholded", thresholded)

    k = cv2.waitKey(1)
    if k & 0xFF == 27:
        break
    
video.release()
cv2.destroyAllWindows()
