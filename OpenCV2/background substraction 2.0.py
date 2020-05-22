import numpy as np
import cv2

cap=cv2.VideoCapture("vtest.avi")


#method 4
fgbg=cv2.createBackgroundSubtractorKNN()

while True:
    ret, frame= cap.read()
    if frame is None:
        break
    fgmask=fgbg.apply(frame)



    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", fgmask)
    keyboard=cv2.waitKey(30)
    if keyboard=="q":
        break
cap.release()
cv2.destroyAllWindows()