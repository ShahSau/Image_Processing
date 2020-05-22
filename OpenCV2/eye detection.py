import cv2

#run the classifier
face_ascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_ascade=cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
#img=cv2.imread("eye.jpg")
#cap=cv2.VideoCapture("face_video.mp4")
cap=cv2.VideoCapture(0)

while cap.isOpened():
    _,img=cap.read()
    #detect faces in our image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=face_ascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=6)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=3)
        roi_gray=gray[y:y+h, x:x+w]
        roi_color=img[y:y+h, x:x+w]
        eyes=eye_ascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (255,255,0), thickness=5)



    cv2.imshow("baby face", img)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()