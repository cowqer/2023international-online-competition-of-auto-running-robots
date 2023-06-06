# 颜色分离 -> 图像腐蚀 -> 获取目标

import cv2
import numpy as np
import sys
import os

local_pic_path = ['../images/03.jpg','../images/04.jpg']

cv2.namedWindow('Canny',cv2.WINDOW_NORMAL)


#定义回调函数
def nothing(x):
    pass

#创建滑动条，分别对应Canny的两个阈值
# cv2.createTrackbar('threshold1','Canny',0,500,nothing)
# cv2.createTrackbar('threshold2','Canny',0,500,nothing)
cv2.createTrackbar('ii','Canny',0,1,nothing)


def detect(img):
    # 转换 HSV 色彩空间
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 通过 HSV 对应的绿色色彩区间对绿色部分进行提取
    lower = np.array([37,77,46])
    upper = np.array([99,255,255])
    lower = np.array([h_l,s_l,v_l])
    upper = np.array([h_h,s_h,v_h])
    mask = cv2.inRange(hsv, lower, upper)

    # 图像腐蚀 去除一些干扰小区域 只保留最大的绿色板
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel)

    # 获取坐标和长度
    index_x = np.where(mask.sum(0) > 0)[0]
    index_y = np.where(mask.sum(1) > 0)[0]
    offset = 5
    if len(index_x) and len(index_y):
        x0 = index_x[0] + offset
        x1 = index_x[-1] - offset
        y1 = index_y[-1] - offset
        return x1-x0, x0, y1
    else:
        return 0, 0, 0
    
THRESHOLE_VALUE=60
COEFFICIENT=0.02
while(1):
    
    #返回当前阈值
    # img_output = img
    # threshold1=cv2.getTrackbarPos('threshold1','Canny')
    # threshold2=cv2.getTrackbarPos('threshold2','Canny')
 
    # h_l = cv2.getTrackbarPos('h_l','Canny')
    # s_l = cv2.getTrackbarPos('s_l','Canny')
    # v_l = cv2.getTrackbarPos('v_l','Canny')
    # h_h = cv2.getTrackbarPos('h_h','Canny')
    # s_h = cv2.getTrackbarPos('s_h','Canny')
    # v_h = cv2.getTrackbarPos('v_h','Canny')
    ii = cv2.getTrackbarPos('ii','Canny')

    img = cv2.imread(local_pic_path[ii])
    
    output_img = img.copy()
    output_img = img.copy()
        # output_img_2 = img_2.copy()
    
    h_l,s_l,v_l =  50,80,25
    h_h,s_h,v_h  = 90,105,80
    
    x,y,r = (int(g) for g in detect(img))
  
 

    # cv2.circle(output_img, (x, y), 3, (225, 0, 0), 5)
    # cv2.circle(output_img, (x, y), r, (225, 0, 0), 3)

    
    img_yellow=cv2.inRange(img,(h_l,s_l,v_l),(h_h,s_h,v_h))
    # cv2.imshow('img_original',img_original)
    
    img_yellow = cv2.medianBlur(img_yellow, 5)
    
    # #膨胀操作，因为是对线条进行提取定位，所以腐蚀可能会造成更大间隔的断点，将线条切断，因此仅做膨胀操作
    # kernel = np.ones((5, 5), np.uint8)
    # img_yellow  = cv2.dilate(img_yellow , kernel, iterations=1)

    #获取图像轮廓坐标，其中contours为坐标值，此处只检测外形轮廓
    contours, hierarchy = cv2.findContours(img_yellow , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
    #cv2.boundingRect()返回轮廓矩阵的坐标值，四个值为x, y, w, h， 其中x, y为左上角坐标，w,h为矩阵的宽和高
        boxes = [cv2.boundingRect(c) for c in contours]
        for box in boxes:
            x, y, w, h = box
            #绘制矩形框对轮廓进行定位
            if w*h > 400:
                cv2.rectangle(output_img, (x, y), (x+w, y+h), (153, 153, 0), 2)
                cv2.circle(output_img,(x, y+h),w,(225, 0, 0), 3)
                print(x, y+h)
            #将绘制的图像保存并展示
            # cv2.imwrite(save_image, img)
            # cv2.imshow('image', img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
   
    # img_yellow = cv2.Canny(img_yellow,50,200)
    
    # img_yellow = cv2.threshold(img_yellow, THRESHOLE_VALUE, 255, cv2.THRESH_BINARY_INV)[1]
    #返回图片和图中轮廓信息，列表形式返回到cnts中
    # 查找轮廓
     
    # contours, _ = cv2.findContours(img_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # json_res = []
    # # mask = np.zeros(img.shape)
    # for c in contours:
    #     # 过滤小面积
    #     scale=100
    #     if (cv2.contourArea(c) < scale ** 2):
    #         continue
 
    #     rect = cv2.minAreaRect(c)
    #     box = cv2.boxPoints(rect)
    #     box = np.int0(box)
    #     # cv2.drawContours(mask, [c], 0, (0, 0, 255))
    #     print(box)
        
    #     cv2.drawContours(output_img, [c], 0, (0, 0, 255))



    
    # cv2.imshow('Canny',img_yellow)
    # cv2.imshow('Canny_2',output_img)
    
    #空格跳出
    if cv2.waitKey(1)==ord(' '):
        break

    #摧毁所有窗口
cv2.destroyAllWindows()


