import cv2
import numpy as np
from matplotlib import pyplot as plt

#img=np.zeros((200,200), np.uint8)
img=cv2.imread("lena.jpg")

#cv2.rectangle(img, (0,100), (200,200), (255), -1)
#cv2.rectangle(img, (0,50), (100,100), (127), -1)
b, g, r=cv2.split(img)


cv2.imshow("img", img)
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)


plt.hist(b.ravel(), 256, [0,256])
plt.hist(g.ravel(), 256, [0,256])
plt.hist(r.ravel(), 256, [0,256])
plt.show()


cv2.waitKey(0)
cv2.drawContours()

