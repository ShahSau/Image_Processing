import matplotlib.pylab as plt
import cv2
import numpy as np

def region_of_interest(img, verticies):
    mask=np.zeros_like(img)
    #chanel_count=img.shape[2]
    match_mask_color=255
    cv2.fillPoly(mask, verticies, match_mask_color)
    masked_img=cv2.bitwise_and(img,mask)
    return masked_img

def draw_the_lines(img, lines):
    img=np.copy(img)
    blank_image=np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blank_image,(x1,y1), (x2,y2), (0,255,255), thickness=4)
    img= cv2.addWeighted(img, 0.8, blank_image, 1.0, 0.0)
    return img
#image=cv2.imread("road_main.png")
#image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
def process(image):

    print(image.shape)
    height=image.shape[0]
    width=image.shape[1]

    region_of_interset_verticies=[
        (0, height),
        (width/1.8, height/1.8),
        (width, height)
    ]

    gray_image=cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny_image=cv2.Canny(gray_image, 80, 100)
    croped_image=region_of_interest(canny_image,np.array([region_of_interset_verticies], np.int32))

    lins=cv2.HoughLinesP(croped_image, rho=6, theta=np.pi/60, threshold=160, lines=np.array([]), minLineLength=40, maxLineGap=25)

    image_with_lines=draw_the_lines(image, lins)
    return image_with_lines

cap=cv2.VideoCapture("solidWhiteRight.mp4")

while(cap.isOpened()):
    ret,frame=cap.read()
    frame=process(frame)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()