
import cv2
import numpy as np
import sys
import os

# img = cv2.imread('/home/k8s/learn_opencv/images/01.jpg')
local_pic_path = ['../images/09.jpg','../images/10.jpg']

#定义回调函数
def nothing(x):
    pass
cv2.namedWindow('Canny',cv2.WINDOW_NORMAL)
cv2.createTrackbar('ii','Canny',0,1,nothing)

def detect(readimg):
    Canny1,Canny2 = 500,235
    param1,param2 = 1,16
    a,b=0,0
    minRadius,maxRadius = 0,26
    dd,ee=4,3
    
    
    kernel = np.ones((3, 3), dtype=np.uint8)
    erosion = cv2.erode(readimg.copy(), kernel, iterations=ee)
    
    kernel = np.ones((3, 3), dtype=np.uint8)
    dilate = cv2.dilate(erosion, kernel, iterations=dd) # 1:迭代次数，也就是执行几次膨胀操作
    
    # try:
    canny = cv2.Canny(dilate, Canny1, Canny2)
    
    # cv2.imshow("canny", canny)
    # 圆形检测
    circles = cv2.HoughCircles(
        canny, cv2.HOUGH_GRADIENT, 1, 30, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

    if circles is None:
        return 0, 0, 0
    else:
        return circles[0, 0, 2], circles[0, 0, 0], circles[0, 0, 1]
    # except:
    #     return 0, 0, 0


while(1):
    


    ii = cv2.getTrackbarPos('ii','Canny')

    img = cv2.imread(local_pic_path[ii])
    
    output_img = img.copy()
   
        
    r, x, y = (int(x) for x in detect(img))
  
    cv2.circle(output_img, (x, y), 3, (225, 124, 56), 2)
    cv2.circle(output_img, (x, y), r, (225, 0, 0), 1)
        
    cv2.imshow('GG',output_img)
    print(r, x, y)
    # cv2.imshow('Canny_2',cv2.Canny(img, threshold1,threshold2))
 
    if cv2.waitKey(1)==ord(' '):
        break

    #摧毁所有窗口
cv2.destroyAllWindows()


