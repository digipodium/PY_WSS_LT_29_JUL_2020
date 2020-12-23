# pip install opencv-contrib-python

import cv2 as cv

cap = cv.VideoCapture(0)
while True:
    status, frame = cap.read()
    if not status:
        print('camera device not working')
        break
    
    cv.imshow("webcam 1", frame)
    if cv.waitKey(1) == ord('q'):
        print('stopping webcam')
        break
cap.release()
cv.destroyAllWindows()