import cv2

#run the classifier
face_ascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("baby_image.jpg")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces in our image
faces=face_ascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=3)


cv2.imshow("baby face", img)
cv2.waitKey()
cv2.destroyAllWindows()