import cv2

face_classifier= cv2.CascadeClassifier('C:/Users/Priya/PycharmProjects/pythonProject/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')


cap=cv2.VideoCapture(0)
while True:
    p,face=cap.read()
    gray=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray,1.1,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(face,(x,y),(x+w,y+h),(266,0,0),2)
        


    cv2.imshow('img',face)
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()




