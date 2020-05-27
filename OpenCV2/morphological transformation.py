import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("smarties.png", 0)
#thresolding
_,mask=cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

#dilation
kernel= np.ones((5,5), np.uint8)
dilation=cv2.dilate(mask, kernel, iterations=3)

#errision
erosion=cv2.erode(mask,kernel,iterations=1)

#opening
opening=cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

#closing
closing=cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

#morphological gradient
md=cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)

#tophat
th=cv2.morphologyEx(mask, cv2.MORPH_CROSS, kernel)
###################
titles=["image", "mask","dilation","errision", "opening","closing","Gradient","tophat"]
images=[img, mask, dilation, erosion,opening,closing,md,th]


for i in range(8):
    plt.subplot(3,3,i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])


plt.show()