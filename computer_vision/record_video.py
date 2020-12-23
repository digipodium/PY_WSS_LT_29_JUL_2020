import cv2 as cv

cap = cv.VideoCapture(0)
encoder = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',encoder,24, (640,480))

while True:
    st, frame = cap.read()
    if not st:
        break
    out.write(frame)
    cv.imshow('recording...',frame)
    if cv.waitKey(1) == ord('c'):
        break
out.release()
cap.release()
cv.destroyAllWindows()