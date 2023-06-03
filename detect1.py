from threading import local
import cv2
import numpy as np
import sys
import os

# img = cv2.imread('/home/k8s/learn_opencv/images/01.jpg')
local_pic_path = ['../images/01.jpg','../images/02.jpg']
# img = cv2.imread('/home/k8s/learn_opencv/images/01.jpg')
#创建窗口
# size = img.shape
# w = size[1] #宽度
# h = size[0] #高度
# print(w,h)
cv2.namedWindow('AA',cv2.WINDOW_NORMAL)
cv2.namedWindow('Canny',cv2.WINDOW_NORMAL)
# cv2.namedWindow('Canny_2',cv2.WINDOW_NORMAL)
# cv2.namedWindow('Canny')
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
# img = cv2.resize(img, (600, 450))
# size = img.shape
# w = size[1] #宽度
# h = size[0] #高度
# print(w,h)
# cv2.resizeWindow("canny", 50, 50)


#定义回调函数
def nothing(x):
    pass

#创建滑动条，分别对应Canny的两个阈值
cv2.createTrackbar('threshold1','Canny',100,500,nothing)
cv2.createTrackbar('threshold2','Canny',100,500,nothing)
cv2.createTrackbar('param1','Canny',50,60,nothing)
cv2.createTrackbar('param2','Canny',100,200,nothing)
cv2.createTrackbar('a','Canny',1,5,nothing)
cv2.createTrackbar('b','Canny',100,255,nothing)
cv2.createTrackbar('minRadius','Canny',0,255,nothing)
cv2.createTrackbar('maxRadius','Canny',0,255,nothing)
cv2.createTrackbar('ii','Canny',0,1,nothing)

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
    if param2<50:
        param2 = 50
    circles = cv2.HoughCircles(
        canny, cv2.HOUGH_GRADIENT, 1, 100, param1=20, param2=40, minRadius=20, maxRadius=100)
# canny, cv2.HOUGH_GRADIENT, 1, 100, param1=37, param2=1, minRadius=0, maxRadius=200)
        
# 测内侧圆心的累加器图像的分辨率于输入图像之比的倒数，如dp=1，累加器和输入图像具有相同的分辨率，
# 如果dp=2，累计器便有输入图像一半那么大的宽度和高度
# minDist表示两个圆之间圆心的最小距离
# param1有默认值100，它是method设置的检测方法的对应的参数，
# 对当前唯一的方法霍夫梯度法cv2.HOUGH_GRADIENT，它表示传递给canny边缘检测算子的高阈值，而低阈值为高阈值的一半
# param2有默认值100，它是method设置的检测方法的对应的参数，
# 对当前唯一的方法霍夫梯度法cv2.HOUGH_GRADIENT，它表示在检测阶段圆心的累加器阈值，
# 它越小，就越可以检测到更多根本不存在的圆，而它越大的话，能通过检测的圆就更加接近完美的圆形了
    
    if circles is None:
        return 0, 0, 0
    else:
        return circles[0, 0, 2], circles[0, 0, 0], circles[0, 0, 1]


while(1):


    threshold1=cv2.getTrackbarPos('threshold1','Canny')
    threshold2=cv2.getTrackbarPos('threshold2','Canny')
    param1=cv2.getTrackbarPos('param1','Canny')
    param2=cv2.getTrackbarPos('param2','Canny')
    a=cv2.getTrackbarPos('a','Canny')
    b=cv2.getTrackbarPos('b','Canny')
    minRadius = cv2.getTrackbarPos('minRadius','Canny')
    maxRadius = cv2.getTrackbarPos('maxRadius','Canny')
    
    ii = cv2.getTrackbarPos('ii','Canny')

    img = cv2.imread(local_pic_path[ii])
    try:
        output_img = img.copy()
        # output_img_2 = img_2.copy()
        
        r, x, y = (int(x) for x in detect(img,threshold1,threshold2,param1,param2,a,b,minRadius,maxRadius))
        print(r,x,y)
        cv2.circle(output_img, (x, y), 3, (225, 0, 0), 5)
        cv2.circle(output_img, (x, y), r, (225, 0, 0), 3)
        
        # cv2.circle(output_img_2, (x2, y2), 3, (225, 0, 0), 5)
        # cv2.circle(output_img_2, (x2, y2), r2, (225, 0, 0), 3)
        # cv2.resizeWindow("canny", 50, 50)
        
        cv2.imshow('AA',output_img)
        cv2.imshow('Canny_2',cv2.Canny(img, threshold1,threshold2))

    except:
        pass
    #空格跳出
    if cv2.waitKey(1)==ord(' '):
        break

    #摧毁所有窗口
cv2.destroyAllWindows()


