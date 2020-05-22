import numpy as np
import cv2

img1=np.zeros((250,500,3), np.uint8)
img1=cv2.rectangle(img1,(200,0),(300,100), (255,255,255),-1)
img2=cv2.imread("image_1.jpg")

#ceating Bit
bitAND= cv2.bitwise_and(img2,img1)
bitOR=cv2.bitwise_or(img2,img1)
bitXOR= cv2.bitwise_xor(img2,img1)
bitNOT2= cv2.bitwise_not(img2)
bitNOT1= cv2.bitwise_not(img1)

#finishing bit

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
#cv2.imshow("BIT-AND", bitAND)
cv2.imshow("OR", bitXOR)

cv2.waitKey(0)
cv2.destroyAllWindows()