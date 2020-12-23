# pip install opencv-contrib-python

import cv2 as cv

cap = cv.VideoCapture("C:/Users/xaidi/Videos/Captures/video.mp4")
while True:
    status, frame = cap.read()
    if not status:
        print('camera device not working')
        break
    h = frame.shape[0] // 3
    w = frame.shape[1] // 3
    frame = cv.resize(frame,(w,h))
    print(frame.shape)
    cv.imshow("webcam 1", frame)
    if cv.waitKey(1) == ord('q'):
        print('stopping webcam')
        break
cap.release()
cv.destroyAllWindows()