import cv2
import numpy as np

cap = cv2.VideoCapture(0)
control = cap.isOpened()

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20, (640, 480))

while(control):
    
    ret, frame = cap.read()

        cv2.imshow("video", frame)

        out.write(frame)

        
        cv2.imshow("video", frame)

        if cv2.waitKey(1) & 0xff == ord("q"):
            break

    else:
        break
    
    
cap.release()
out.release()
cv2.destroyAllWindows()
