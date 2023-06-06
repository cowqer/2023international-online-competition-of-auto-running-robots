import cv2
import numpy as np
import sys
import os
import math


def detect(img):
  
    h_l,s_l,v_l =  50,80,25
    h_h,s_h,v_h  = 90,105,80
    img_yellow=cv2.inRange(img,(h_l,s_l,v_l),(h_h,s_h,v_h))
    
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
                # cv2.rectangle(output_img, (x, y), (x+w, y+h), (153, 153, 0), 2)
                # cv2.circle(output_img,(x, y+h),w,(225, 0, 0), 3)
                # print(x, y+h)
                return w,x,y+h
    return 0, 0, 0


