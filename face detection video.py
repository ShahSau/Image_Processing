import cv2

#run the classifier
face_ascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#img=cv2.imread("baby_image.jpg")
#cap=cv2.VideoCapture("face_video.mp4")
cap=cv2.VideoCapture(0)

while cap.isOpened():
    _,img=cap.read()
    #detect faces in our image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=face_ascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=3)


    cv2.imshow("baby face", img)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()