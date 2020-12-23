import cv2 as cv

cap = cv.VideoCapture(0)
while True:
    status, frame = cap.read()
    if not status:
        print('camera device not working')
        break
    framebw = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    framelab = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
    framexyz = cv.cvtColor(frame, cv.COLOR_BGR2XYZ)
    framehsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    framehls = cv.cvtColor(frame, cv.COLOR_BGR2HLS)
    cv.imshow("webcam 1", frame)
    cv.imshow("webcam bw", framebw)
    cv.imshow("webcam lab", framelab)
    cv.imshow("webcam xyz", framexyz)
    cv.imshow("webcam hsv", framehsv)
    cv.imshow("webcam hls", framehls)
    if cv.waitKey(1) == ord('q'):
        print('stopping webcam')
        break
cap.release()
cv.destroyAllWindows()