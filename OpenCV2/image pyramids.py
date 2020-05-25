import cv2
import numpy as np
img=cv2.imread("lena.jpg")
#gaussian
lr1=cv2.pyrDown(img)
lr2=cv2.pyrDown(lr1)
hr2=cv2.pyrUp(img)



cv2.imshow("original image", img)
cv2.imshow("pyrdown1", lr1)
cv2.imshow("pyrdown2", lr2)
cv2.imshow("up1",hr2)

cv2.waitKey(0)
cv2.destroyAllWindows()