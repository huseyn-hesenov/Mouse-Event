import cv2 as cv
import numpy as np
def draw(event,x,y,flags,param):
    if(event==cv.EVENT_LBUTTONDOWN):
        cv.circle(img,(x,y),20,(255,255,255),3)
    pass

img=np.ones((512,512,3),np.uint8)
cv.namedWindow("mouse")
cv.setMouseCallback("mouse",draw)
while(1):
    cv.imshow("mouse",img)
    if(cv.waitKey(1) & 0xFF==ord("q")):
        print("exited program")
        break
cv.destroyAllWindows()