import cv2
import numpy as np

img= cv2.imread("gradient.png",0)
#Binary thresholding
_,th1=cv2.threshold(img, 127,255,cv2.THRESH_BINARY)
#Binary inverse thresholding
_,th2=cv2.threshold(img, 127,255,cv2.THRESH_BINARY_INV)
#thresh trunC
_,th3=cv2.threshold(img, 127,255,cv2.THRESH_TRUNC)
#thresh to zero
_,th4=cv2.threshold(img, 127,255,cv2.THRESH_TOZERO)
#thresh to zero inverse
_,th5=cv2.threshold(img, 127,255,cv2.THRESH_TOZERO_INV)


cv2.imshow("Image", img)
cv2.imshow("TRhresholding", th1)
cv2.imshow("TRhresholding22", th2)
cv2.imshow("Trunc",th3)
cv2.imshow("Zero",th4)
cv2.imshow("ZeroONV",th5)
cv2.waitKey(0)
cv2.destroyAllWindows()