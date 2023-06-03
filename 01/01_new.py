import cv2
import numpy as np
import sys
import os

# img = cv2.imread('/home/k8s/learn_opencv/images/01.jpg')
img = cv2.imread('/home/k8s/learn_opencv/images/01.jpg')
#创建窗口
# cv2.resizeWindow("canny", 50, 50)


#定义回调函数
def nothing(x):
    pass

#创建滑动条，分别对应Canny的两个阈值
cv2.createTrackbar('threshold1','Canny',0,500,nothing)
cv2.createTrackbar('threshold2','Canny',0,500,nothing)
cv2.createTrackbar('param1','Canny',0,255,nothing)
cv2.createTrackbar('param2','Canny',0,255,nothing)
cv2.createTrackbar('a','Canny',0,255,nothing)
cv2.createTrackbar('b','Canny',0,255,nothing)
cv2.createTrackbar('minRadius','Canny',0,255,nothing)
cv2.createTrackbar('maxRadius','Canny',0,255,nothing)

def detect(readimg,Canny1,Canny2,param1,param2,a,b,minRadius,maxRadius):
    # Canny 边缘检测
    
    # Canny1 = 0
    # Canny2 =[94,++] [129,140] +
    # param1 = 
    # param2 = [0,21]
    # b = 
    # minRadius = [11]
    # maxRadius = [44] 
    
    canny = cv2.Canny(readimg, Canny1,Canny2)
# 
    # 圆形检测
    circles = cv2.HoughCircles(
        canny, cv2.HOUGH_GRADIENT, a, b, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

   
    
    print(circles[0, 0, 2], circles[0, 0, 0], circles[0, 0, 1])
    if circles is None:
        return 0, 0, 0
    else:
        return circles[0, 0, 2], circles[0, 0, 0], circles[0, 0, 1]


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
    # img_output=cv2.Canny(img,threshold1,threshold2)

    #显示图片
    # r, x, y = (int(x) for x in detect(img,threshold1,threshold2))

    # 绘制结果
    try:
        output_img = img.copy()
        # output_img_2 = img_2.copy()
        
        r, x, y = (int(x) for x in detect(img,threshold1,threshold2,param1,param2,a,b,minRadius,maxRadius))
        
        # r2, x2, y2 = (int(x) for x in detect(img_2,threshold1,threshold2,param1,param2,a,b))

 

        cv2.circle(output_img, (x, y), 3, (225, 0, 0), 5)
        cv2.circle(output_img, (x, y), r, (225, 0, 0), 3)
        
        # cv2.circle(output_img_2, (x2, y2), 3, (225, 0, 0), 5)
        # cv2.circle(output_img_2, (x2, y2), r2, (225, 0, 0), 3)
        # cv2.resizeWindow("canny", 50, 50)
    
        
        cv2.imshow('Canny',output_img)
        cv2.imshow('Canny_2',cv2.Canny(img, threshold1,threshold2))
        # concatanate image Horizontally

        # cv2.imshow('Canny',output_img_2)
        
    except:
        pass
    #空格跳出
    if cv2.waitKey(1)==ord(' '):
        break

    #摧毁所有窗口
cv2.destroyAllWindows()


