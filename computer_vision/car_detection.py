import cv2 as cv

 
car_cascade = cv.CascadeClassifier('computer_vision/cars.xml')
img = cv.imread('computer_vision/road.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cars = car_cascade.detectMultiScale(gray, 1.1, 1)
print('found',len(cars))
for (x,y,w,h) in cars:
        cv.rectangle(img, (x,y),(x+w,y+h),(255,100,100),2)
cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()