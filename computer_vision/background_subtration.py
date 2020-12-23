import cv2 as cv

cap = cv.VideoCapture(0)
bgmask = cv.createBackgroundSubtractorMOG2()
while True:
    status, frame = cap.read()
    if not status:
        print('camera device not working')
        break
    mask = bgmask.apply(frame)
    cv.imshow("webcam 1", frame)
    cv.imshow("webcam 2", mask)
    if cv.waitKey(1) == ord('q'):
        print('stopping webcam')
        break
cap.release()
cv.destroyAllWindows()