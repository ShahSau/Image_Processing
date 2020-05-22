import cv2
import datetime

cap= cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    datet= str(datetime.datetime.now())
    font= cv2.FONT_HERSHEY_SIMPLEX
    frame= cv2.putText(frame, datet, (10,50),font, 1, (0,255,255), 10, cv2.LINE_AA)
    cv2.imshow("VIDEO",frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()