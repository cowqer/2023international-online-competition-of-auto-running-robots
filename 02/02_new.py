# 边缘检测 -> 轮廓检测 -> 矩形拟合 -> 筛选目标
import cv2
import numpy as np
import sys
import os
import math

# img = cv2.imread('/home/k8s/learn_opencv/images/01.jpg')
# img = cv2.imread('/home/k8s/learn_opencv/images/03.jpg')

local_pic_path = ['../images/03.jpg','../images/04.jpg']
#创建窗口
# size = img.shape
# w = size[1] #宽度
# h = size[0] #高度
# print(w,h)
cv2.namedWindow('Canny',cv2.WINDOW_NORMAL)
cv2.namedWindow('GG',cv2.WINDOW_NORMAL)


# cv2.namedWindow('finger',cv2.WINDOW_NORMAL)
# cv2.namedWindow('finger_canny',cv2.WINDOW_NORMAL)


#定义回调函数
def nothing(x):
    pass

#创建滑动条，分别对应Canny的两个阈值
cv2.createTrackbar('wh_h','Canny',0,2000,nothing)
cv2.createTrackbar('wh_l','Canny',0,2000,nothing)
cv2.createTrackbar('threshold1','Canny',0,500,nothing)
cv2.createTrackbar('threshold2','Canny',0,500,nothing)
cv2.createTrackbar('ii','Canny',0,1,nothing)

def detect(readimg,Canny1,Canny2,wh_l,wh_h):
    
    
    (cx, cy), (width, height) = (0,0),(0,0)
    
    ROI_lower_H,ROI_lower_S,ROI_lower_V = 35,43,46
    ROI_upper_H,ROI_upper_S,ROI_upper_V = 77,255,255
    
    ROI_lower = np.array([ROI_lower_H,ROI_lower_S,ROI_lower_V])
    ROI_upper = np.array([ROI_upper_H,ROI_upper_S,ROI_upper_V])
    
    ROI_image_HSV = cv2.cvtColor(readimg,cv2.COLOR_BGR2HSV)
    # print(type(ROI_image_HSV))
    ROI_mask = cv2.inRange(ROI_image_HSV,ROI_lower,ROI_upper)
    # print(type(ROI_mask))
    if 1 == 1:
        contours, hierarchy = cv2.findContours(ROI_mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        # x,y,w,h = 0,0,img.shape[0],img.shape[1]
        if len(contours)!=0:
            for contour in contours:
                if cv2.contourArea(contour)>800:
                    x,y,w,h = cv2.boundingRect(contour)
                    # if wh_l < w and  wh_l < h and wh_h > w and wh_h > h:
                    if 1==1:
                        # cv2.rectangle(readimg,(x,y),(x+w,y+h),(0,0,255),2)
                        # cv2.rectangle(readimg,(x,y),(readimg.shape[1],readimg.shape[0]),(0,0,255),2) ROI
                        pass
                        # cv2.imshow(img)
        flag = 0
    else:
        pass
    cv2.imshow("XX",readimg)
    
    GG = readimg.copy()
    GG = GG[x:readimg.shape[0],y:readimg.shape[1]]
    
    # kernel = np.ones((3, 3), dtype=np.uint8)
    # erosion = cv2.erode(GG.copy(), kernel, iterations=1)
    # ss = np.hstack((img, erosion))
    
    kernel = np.ones((3, 3), dtype=np.uint8)
    dilate = cv2.dilate(GG.copy(), kernel, 1) # 1:迭代次数，也就是执行几次膨胀操作
    
    kernel = np.ones((3, 3), dtype=np.uint8)
    erosion = cv2.erode(dilate, kernel, iterations=1)
    erosion = cv2.cvtColor(erosion,cv2.COLOR_BGR2GRAY)
    
    # erosion = cv2.Canny(erosion,wh_l,wh_h)
    erosion = cv2.Canny(erosion,132,302)
    
    cv2.imshow("ROI_erosion",erosion)  ## canny 28,63
    
    ROI_contours, ROI_hier = cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    Point_list=[]
    
    ans=[]
    for cidx,cnt in enumerate(ROI_contours):
        ((cx, cy), (width, height), theta) = cv2.minAreaRect(cnt)
        minAreaRect = ((cx, cy), (width, height), theta)
        # 将浮点数坐标转换成整数
        rectCnt = np.int64(cv2.boxPoints(minAreaRect))
            
        rectCnt = np.array([rectCnt[0].tolist(),rectCnt[1].tolist(),rectCnt[2].tolist(),rectCnt[3].tolist()])

        area = width * height
        # cv2.drawContours(GG, [rectCnt], 0, (0,255,0), 3)
        # cv2.rectangle(erosion,(cx,cy),(0,0,255),2)
        if area >1000 and width < 3 * height and height < 3 * width : #and area <8000: #and width < 2 * height and height < 2 * width :  #132 364
        # if 1==1:
            cv2.drawContours(GG, [rectCnt], 0, (0,255,0), 3)
            Point_list.append(rectCnt)
            
            mid_point_y ,mid_point_x =  0 , 0
        
            mid_point_x = int((Point_list[0][0][0]+Point_list[0][1][0]+Point_list[0][2][0]+Point_list[0][3][0])/4)
            mid_point_y = int((Point_list[0][0][1]+Point_list[0][1][1]+Point_list[0][2][1]+Point_list[0][3][1])/4)
            
            x1,x2,y1,y2,r=0,0,0,0,0
            for index,value in enumerate(Point_list[0]):
                if value[0]<mid_point_x and value[1]>mid_point_y:
                    # print(value[0],value[1])
                    x1,y1 = value[0],value[1]
                
                if value[0]>mid_point_x and value[1]>mid_point_y:
                    x2,y2 = value[0],value[1]
            
            r = math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
            print(int(r),x1+y,y1+x)
            return int(r),x1+y,y1+x
            
    # ans=[]
    # cv2.imshow("GG",GG)
   
    
    
    # aa =  cv2.imread("../images/21.jpg")
    # cv2.imshow("finger",aa)
    # cv2.imshow("finger_GRAY",cv2.cvtColor(aa,cv2.COLOR_BGR2GRAY))
    # cv2.imshow("finger_canny",cv2.Canny(cv2.cvtColor(aa,cv2.COLOR_BGR2GRAY),threshold1,threshold2))
    
    return 0, 0, 0

while(1):
    
    #返回当前阈值
    # img_output = img
    threshold1=cv2.getTrackbarPos('threshold1','Canny')
    threshold2=cv2.getTrackbarPos('threshold2','Canny')
 
    wh_l = cv2.getTrackbarPos('wh_l','Canny')
    wh_h = cv2.getTrackbarPos('wh_h','Canny')
    
    ii = cv2.getTrackbarPos('ii','Canny')

    img = cv2.imread(local_pic_path[ii])
    
    output_img = img.copy()
    #     # output_img_2 = img_2.copy()
        
    x,y,r = (int(g) for g in detect(img,threshold1,threshold2,wh_l,wh_h))
  
 

    cv2.circle(output_img, (x, y), 3, (225, 0, 0), 5)
    cv2.circle(output_img, (x, y), r, (225, 0, 0), 3)

        
    # cv2.imshow('oo',output_img)
    # cv2.imshow('Canny_2',cv2.Canny(img, threshold1,threshold2))
        # concatanate image Horizontally

        # cv2.imshow('Canny',output_img_2)
    #空格跳出
    if cv2.waitKey(1)==ord(' '):
        break

    #摧毁所有窗口
cv2.destroyAllWindows()


