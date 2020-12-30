import cv2 as cv

cap = cv.VideoCapture(0)
faceCascade = cv.CascadeClassifier('computer_vision/face.xml')
eyeCascade = cv.CascadeClassifier('computer_vision/eye.xml')
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
        roi_gray = gray[y:y+h, x:x+w] # grabbing face area from full frame
        roi_color = frame[y:y+h, x:x+w] # grabbing face area from full frame in color
        eyes = eyeCascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color, (ex,ey),(ex+ew,ey+eh),(255,0,255),1)
    
        
    cv.imshow("webcam 1", frame)
    if cv.waitKey(1) == ord('q'):
        print('stopping webcam')
        break
cap.release()
cv.destroyAllWindows()