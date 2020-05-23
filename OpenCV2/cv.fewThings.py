import numpy as np
import cv2

img =cv2.imread("messi5.jpg")
img2=cv2.imread("opencv-logo.png")

print(img.shape) #returns a tuple of number of rows, columns, channels
print(img.size) #returns Total number of pixels is accessed
print(img.dtype) #returns Image datatype is obtained
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

#ROI START
#creating a ball variable using real ball coordinates
ball= img[280:340, 330:390] #280:340 and 330:390, 273:333, 100:160are jjust the coordinates
#putting the ball in a specific coordinates
img[273:333, 100:160]=ball
#ROI ENNDS

#resize start
img= cv2.resize(img, (512,512))
img2=cv2.resize(img2, (512,512))
#resize ends

#ADD 2 Images
dst=cv2.add(img,img2)
#finish ADD 2 IMAGES

#ADDWEIGHTED METHOD
dst2=cv2.addWeighted(img,.5,img2,.5,0)
#ADDWEIGHTED METHOD FUNNISH
cv2.imshow("image", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
