import cv2 as cv

cap = cv.VideoCapture(0)
faceCascade = cv.CascadeClassifier('computer_vision/face.xml')
while True:
    status, frame = cap.read()
    if not status:
        print('camera device not working')
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor = 1.1,
                minNeighbors=5,
                minSize=(30,30))

    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y),(x+w,y+h),(255,100,100),2)
        
    cv.imshow("webcam 1", frame)
    if cv.waitKey(1) == ord('q'):
        print('stopping webcam')
        break
cap.release()
cv.destroyAllWindows()