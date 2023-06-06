import cv2
import numpy as np
import sys
import os
import math

local_pic_path = ['../images/05.jpg','../images/06.jpg']
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
# cv2.createTrackbar('wh_h','Canny',0,50,nothing)
cv2.createTrackbar('wh_l','Canny',166,500,nothing)
# cv2.createTrackbar('threshold1','Canny',1,5,nothing)
# cv2.createTrackbar('threshold2','Canny',116,500,nothing)
# cv2.createTrackbar('dd','Canny',1,5,nothing)
# cv2.createTrackbar('ee','Canny',1,5,nothing)
cv2.createTrackbar('ii','Canny',0,1,nothing)


def detect(img,wh_l):

    h_l,s_l,v_l =  50,80,25
    h_h,s_h,v_h  = 90,105,80
    img_yellow=cv2.inRange(img,(h_l,s_l,v_l),(h_h,s_h,v_h))
    
    img_yellow = cv2.medianBlur(img_yellow, 1)
    
    
    cv2.imshow("img_yellow",img_yellow)
    
    GG =img.copy()
    
    
    contours, hierarchy = cv2.findContours(img_yellow , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

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
        if  w * h > wh_l*200:
            # cv2.drawContours(img, [rect], 0, (0,255,0), 3)
            # cv2.drawContours(GG, [box], 0, (0,255,0), 3)
            
            cv2.drawContours(GG, [box], 0, (0,255,0), 3)
            box = sorted(box, key=lambda x: x[1])
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
    # threshold1=cv2.getTrackbarPos('threshold1','Canny')
    # threshold2=cv2.getTrackbarPos('threshold2','Canny')
 
    wh_l = cv2.getTrackbarPos('wh_l','Canny')
    # wh_h = cv2.getTrackbarPos('wh_h','Canny')
    
    # dd = cv2.getTrackbarPos('dd','Canny')
    # ee = cv2.getTrackbarPos('ee','Canny')
    
    ii = cv2.getTrackbarPos('ii','Canny')

    img = cv2.imread(local_pic_path[ii])
    
    output_img = img.copy()
    # cv2.imshow("kk",output_img)
    #     # output_img_2 = img_2.copy()
        
    r,x,y = (int(g) for g in detect(output_img,wh_l))
    print(r,x,y)
 
    if cv2.waitKey(1)==ord(' '):
        break

    #摧毁所有窗口
cv2.destroyAllWindows()