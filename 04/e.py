import cv2 as cv
import cv2
import math
import numpy as np

def detect(PIC_PATH):
    
    (cx, cy), (width, height) = (0,0),(0,0)
    
    ROI_lower_H,ROI_lower_S,ROI_lower_V = 100,84,134
    ROI_upper_H,ROI_upper_S,ROI_upper_V = 150,255,255
    
    ROI_lower = np.array([ROI_lower_H,ROI_lower_S,ROI_lower_V])
    ROI_upper = np.array([ROI_upper_H,ROI_upper_S,ROI_upper_V])
    
    ROI_image_HSV = cv2.cvtColor(PIC_PATH,cv2.COLOR_BGR2HSV)
    ROI_mask = cv2.inRange(ROI_image_HSV,ROI_lower,ROI_upper)
    
    # 寻找轮廓
    ROI_contours, ROI_hier = cv2.findContours(ROI_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    Point_list=[]
    
    for cidx,cnt in enumerate(ROI_contours):
        ((cx, cy), (width, height), theta) = cv2.minAreaRect(cnt)
        minAreaRect = ((cx, cy), (width, height), theta)
        # 将浮点数坐标转换成整数
        rectCnt = np.int64(cv2.boxPoints(minAreaRect))
            
        rectCnt = np.array([rectCnt[0].tolist(),rectCnt[1].tolist(),rectCnt[2].tolist(),rectCnt[3].tolist()])

        area = width * height
        
        if area >300 and area < 1500 and width < 1.5* height and height < 1.5 * width :
            Point_list.append(rectCnt)
    ans=[]
    
    if Point_list[1][0][0]<Point_list[0][0][0]:
        
        mid_point_y ,mid_point_x =  0 , 0
        
        mid_point_x = int((Point_list[1][0][0]+Point_list[1][1][0]+Point_list[1][2][0]+Point_list[1][3][0])/4)
        mid_point_y = int((Point_list[1][0][1]+Point_list[1][1][1]+Point_list[1][2][1]+Point_list[1][3][1])/4)
        
        for index,value in enumerate(Point_list[1]):
            if value[0]>mid_point_x and value[1]>mid_point_y:
                ans.append(value)
                
        #############        
        mid_point_y ,mid_point_x =  0 , 0
        
        mid_point_x = int((Point_list[0][0][0]+Point_list[0][1][0]+Point_list[0][2][0]+Point_list[0][3][0])/4)
        mid_point_y = int((Point_list[0][0][1]+Point_list[0][1][1]+Point_list[0][2][1]+Point_list[0][3][1])/4)
        
        for index,value in enumerate(Point_list[0]):
            if value[0]<mid_point_x and value[1]>mid_point_y:
                ans.append(value)
        
    elif Point_list[1][0][0]>Point_list[0][0][0]:
        
        mid_point_y ,mid_point_x =  0 , 0
        
        mid_point_x = int((Point_list[0][0][0]+Point_list[0][1][0]+Point_list[0][2][0]+Point_list[0][3][0])/4)
        mid_point_y = int((Point_list[0][0][1]+Point_list[0][1][1]+Point_list[0][2][1]+Point_list[0][3][1])/4)
        
        for index,value in enumerate(Point_list[0]):
            if value[0]>mid_point_x and value[1]>mid_point_y:
                ans.append(value)
                
        #############        
        mid_point_y ,mid_point_x =  0 , 0
        
        mid_point_x = int((Point_list[1][0][0]+Point_list[1][1][0]+Point_list[1][2][0]+Point_list[1][3][0])/4)
        mid_point_y = int((Point_list[1][0][1]+Point_list[1][1][1]+Point_list[1][2][1]+Point_list[1][3][1])/4)
        
        for index,value in enumerate(Point_list[1]):
            if value[0]<mid_point_x and value[1]>mid_point_y:
                ans.append(value)

    else:
        pass
    
    
    if len(ans) == 0:
        return 0,0,0
    
    a = math.pow(ans[0][1]-ans[1][1],2)
    b = math.pow(ans[0][0]-ans[1][0],2)
    r = math.sqrt(a+b)
    r = int(r)

    return r,ans[0][0],ans[0][1]

GG = cv2.imread("../images/08.jpg")
r, x1, y1 = detect(GG)
print(r, x1, y1)