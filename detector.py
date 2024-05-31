import cv2

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cardDetector = cv2.CascadeClassifier('./classifier/cascade.xml')

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    card = cardDetector.detectMultiScale(gray,
                                       scaleFactor=3.8,
                                       minNeighbors=150,
                                       minSize=(70,78))
    
    for (x,y,w,h) in card:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,'Carta de yugioh',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) == 27:
        break
cam.release()
cv2.destroyAllWindows()