import cv2
import numpy as np
import math

ix,iy = -1,-1
firstx,firsty = 0,0
k=0
distance=0
# mouse callback function
    
def draw_point(event,x,y,flags,param):
    global ix,iy,firstx,firsty
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),1,(255,0,0),-1)
        ix,iy = x,y


img = cv2.imread("save.jpg",1)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_point)


cv2.setMouseCallback('image',draw_point) 

while(1):
    cv2.imshow('image',img)
    j = cv2.waitKey(20) & 0xFF
    if j == 27:
        break
    elif j == ord('a'):
        if(k==0):
                [firstx, firsty] = [ix,iy]
                print firstx, firsty
                print 'Entering firstx firsty'
                k=k+1
        else:
                print ix,iy
                print 'Entering ix iy'
                distance=math.sqrt(((ix-firstx)*(ix-firstx))+((iy-firsty)*(iy-firsty)))
                print distance
cv2.destroyAllWindows()
