# how to break the loop with a key 
# can u also check this 

import cv2
import time 
import numpy as np
from numpy.lib.type_check import imag 

fourcc=cv2.VideoWriter_fourcc(*"XVID")
outputfile=cv2.VideoWriter("output.avi",fourcc,20,(640,480))
frame=cv2.resize(frame,(640,480))
img=cv2.resize(img,(640,480))
capture=cv2.VideoCapture(0)
time.sleep(2)
bg=0

for i in range(60):
    ret,bg=capture.read()

bg=np.flip(bg,axis=1)

while(capture.isOpened()):
    ret,img=capture.read()
    if not ret:
        break
    img=np.flip(img,axis=1)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    u_black=np.arr([104,153,70])
    l_black=np.array(([30,30,0]))
    mask=cv2.inRange(frame,l_black,u_black)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    f=frame-res
    f=np.where(f==0,img,f)
    
    finalOutput=cv2.addWeighted(res,1,mask,1,0)
    outputfile.write(finalOutput)
    cv2.imshow("magic",finalOutput)
    cv2.waitKey(1)
capture.release()
cv2.destroyAllWindows()
