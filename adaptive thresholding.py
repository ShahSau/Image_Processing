import cv2
import numpy as np

img=cv2.imread("sudoku.png",0)

#adaptive thresholding using mean
th2=cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,2)
#adaptive thresholding using Gaussian
th3=cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,2)
cv2.imshow("Image",img)
cv2.imshow("MEAN",th2)
cv2.imshow("GAU",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()