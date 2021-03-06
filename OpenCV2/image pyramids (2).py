import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("lena.jpg")
layer=img.copy()
gp=[layer]

for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
   # cv2.imshow(str(i),layer)

for i in range(5,0,-1):
    gaussain_extend=cv2.pyrUp(gp[i])
    laplacian=cv2.subtract(gp[i-1], gaussain_extend)
    cv2.imshow(str(i), laplacian)

cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()