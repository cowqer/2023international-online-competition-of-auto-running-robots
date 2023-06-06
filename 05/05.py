
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
#创建滑动条，分别对应Canny的两个阈值
cv2.createTrackbar('threshold1','Canny',0,500,nothing)
cv2.createTrackbar('threshold2','Canny',0,500,nothing)
cv2.createTrackbar('param1','Canny',4,5,nothing)
cv2.createTrackbar('param2','Canny',26,50,nothing)
cv2.createTrackbar('a','Canny',0,255,nothing)
cv2.createTrackbar('b','Canny',0,255,nothing)
cv2.createTrackbar('minRadius','Canny',0,255,nothing)
cv2.createTrackbar('maxRadius','Canny',0,255,nothing)
cv2.createTrackbar('dd','Canny',1,5,nothing)
cv2.createTrackbar('ee','Canny',1,5,nothing)
cv2.createTrackbar('ii','Canny',0,1,nothing)

def detect(readimg,Canny1,Canny2,param1,param2,a,b,minRadius,maxRadius,ee,dd):
    #     # canny 边缘检测
    # Canny1,Canny2 = 500,71
    # param1,param2 = 4,26
    # # a,b
    # minRadius,maxRadius = 15,47
    
    
    kernel = np.ones((3, 3), dtype=np.uint8)
    erosion = cv2.erode(readimg.copy(), kernel, iterations=ee)
    
    kernel = np.ones((3, 3), dtype=np.uint8)
    dilate = cv2.dilate(erosion, kernel, iterations=dd) # 1:迭代次数，也就是执行几次膨胀操作
    
    # try:
    canny = cv2.Canny(dilate, Canny1, Canny2)
    
    cv2.imshow("canny", canny)
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
    
    #返回当前阈值
    # img_output = img
    threshold1=cv2.getTrackbarPos('threshold1','Canny')
    threshold2=cv2.getTrackbarPos('threshold2','Canny')
    param1=cv2.getTrackbarPos('param1','Canny')
    param2=cv2.getTrackbarPos('param2','Canny')
    a=cv2.getTrackbarPos('a','Canny')
    b=cv2.getTrackbarPos('b','Canny')
    minRadius = cv2.getTrackbarPos('minRadius','Canny')
    maxRadius = cv2.getTrackbarPos('maxRadius','Canny')
    
    dd = cv2.getTrackbarPos('dd','Canny')
    ee = cv2.getTrackbarPos('ee','Canny')
    ii = cv2.getTrackbarPos('ii','Canny')
    # img_output=cv2.Canny(img,threshold1,threshold2)

    #显示图片
    # r, x, y = (int(x) for x in detect(img,threshold1,threshold2))

    # 绘制结果
   
    ii = cv2.getTrackbarPos('ii','Canny')

    img = cv2.imread(local_pic_path[ii])
    
    output_img = img.copy()
   
        
    r, x, y = (int(x) for x in detect(img,threshold1,threshold2,param1,param2,a,b,minRadius,maxRadius,ee,dd))
        
        # r2, x2, y2 = (int(x) for x in detect(img_2,threshold1,threshold2,param1,param2,a,b))

 

    cv2.circle(output_img, (x, y), 3, (225, 124, 56), 2)
    cv2.circle(output_img, (x, y), r, (225, 0, 0), 1)
        
        # cv2.circle(output_img_2, (x2, y2), 3, (225, 0, 0), 5)
        # cv2.circle(output_img_2, (x2, y2), r2, (225, 0, 0), 3)
        # cv2.resizeWindow("canny", 50, 50)
    
        
    cv2.imshow('GG',output_img)
    print(r, x, y)
    # cv2.imshow('Canny_2',cv2.Canny(img, threshold1,threshold2))
 
    if cv2.waitKey(1)==ord(' '):
        break

    #摧毁所有窗口
cv2.destroyAllWindows()


