import cv2
import numpy as np
import sys
import os
import math

local_pic_path = ['../images/03.jpg','../images/04.jpg']
#创建窗口
# size = img.shape
# w = size[1] #宽度
# h = size[0] #高度
# # print(w,h)
cv2.namedWindow('Canny',cv2.WINDOW_NORMAL)
# cv2.namedWindow('GG',cv2.WINDOW_NORMAL)


# cv2.namedWindow('finger',cv2.WINDOW_NORMAL)
# cv2.namedWindow('finger_canny',cv2.WINDOW_NORMAL)


#定义回调函数
def nothing(x):
    pass

#创建滑动条，分别对应Canny的两个阈值
cv2.createTrackbar('wh_h','Canny',0,50,nothing)
cv2.createTrackbar('wh_l','Canny',166,500,nothing)
cv2.createTrackbar('threshold1','Canny',87,500,nothing)
cv2.createTrackbar('threshold2','Canny',116,500,nothing)
cv2.createTrackbar('dd','Canny',1,5,nothing)
cv2.createTrackbar('ee','Canny',1,5,nothing)
cv2.createTrackbar('ii','Canny',0,1,nothing)


def detect(img,threshold1,threshold2,wh_l,wh_h,dd,ee):
    # canny 边缘检测
    GG = img.copy()
    # edge = cv2.Canny(img, 40, 80)
    
    edge = cv2.Canny(img,threshold1,threshold2)
    
    
    
    kernel = np.ones((3, 3), dtype=np.uint8)
    dilate = cv2.dilate(edge.copy(), kernel, dd) # 1:迭代次数，也就是执行几次膨胀操作
    
    kernel = np.ones((3, 3), dtype=np.uint8)
    erosion = cv2.erode(dilate, kernel, iterations=ee)
    # erosion = cv2.cvtColor(erosion,cv2.COLOR_BGR2GRAY)
    
    # erosion = cv2.Canny(erosion,wh_l,wh_h)
    # erosion = cv2.Canny(erosion,132,302)
    
    # cv2.imshow('oo',img.copy())
    cv2.imshow('bb',erosion)
    # 轮廓检测W
    # contours, _ = cv2.findContours(
    #     edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # ROI_contours, ROI_hier = cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(erosion,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # 遍历轮廓
    for contour in contours:
        # 矩形拟合
        rect = cv2.minAreaRect(contour)
        
        
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        x, y, w, h = cv2.boundingRect(contour)
        
        
        # cv2.drawContours(GG, [box], 0, (0,255,0), 3)
        # cv2.imshow("img",GG)
        # 目标筛选
        # if 50000 > w * h > 18000:
        if  w * h > wh_l*100:
            # cv2.drawContours(img, [rect], 0, (0,255,0), 3)
            # cv2.drawContours(GG, [box], 0, (0,255,0), 3)
            
            cv2.drawContours(GG, [box], 0, (0,255,0), 3)
            # box = sorted(box, key=lambda x: x[1])
            line = sorted(box[-2:], key=lambda x: x[0])
            # # cv2.drawContours(img, [box], 0, (0,255,0), 3)
            # # cv2.imshow("imgg",img)
            cv2.imshow("img",GG)
            return np.sqrt(np.power(line[0] - line[1], 2).sum()), line[0][0], line[0][1]
    # 0 35 76 101 1 1  1
    
    return 0, 0, 0

while(1):
    
    #返回当前阈值
    # img_output = img
    threshold1=cv2.getTrackbarPos('threshold1','Canny')
    threshold2=cv2.getTrackbarPos('threshold2','Canny')
 
    wh_l = cv2.getTrackbarPos('wh_l','Canny')
    wh_h = cv2.getTrackbarPos('wh_h','Canny')
    
    dd = cv2.getTrackbarPos('dd','Canny')
    ee = cv2.getTrackbarPos('ee','Canny')
    
    ii = cv2.getTrackbarPos('ii','Canny')

    img = cv2.imread(local_pic_path[ii])
    
    output_img = img.copy()
    #     # output_img_2 = img_2.copy()
        
    r,x,y = (int(g) for g in detect(img,threshold1,threshold2,wh_l,wh_h,dd,ee))
    print(r,x,y)
 

    # cv2.circle(output_img, (x, y), 3, (225, 0, 0), 5)
    # cv2.circle(output_img, (x, y), r, (225, 0, 0), 3)

        
    # cv2.imshow('oo',output_img)
    # cv2.imshow('Canny_2',cv2.Canny(img, threshold1,threshold2))
        # concatanate image Horizontally

        # cv2.imshow('Canny',output_img_2)
    #空格跳出
    if cv2.waitKey(1)==ord(' '):
        break

    #摧毁所有窗口
cv2.destroyAllWindows()