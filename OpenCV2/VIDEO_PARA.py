import cv2

cap= cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1300)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while(True):
    ret, frame= cap.read()
    if ret == True:
        #cv2.imshow("VIDEO", frame)
        gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("WIND", gray)
        if cv2.waitKey(1) == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()