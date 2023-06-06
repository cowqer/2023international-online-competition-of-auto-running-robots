import cv2 as cv
import cv2

import numpy as np
from prometheus_client import Counter
from pyrsistent import v

# ```
# hue 
# s
# v
# ````
#定义回调函数
def nothing(x):
    pass

lower = np.array([320,40,60])
upper = np.array([330,50,80])

a = {}
a[0] = cv2.imread('/home/k8s/learn_opencv/images/07.jpg')
a[1] = cv2.imread('/home/k8s/learn_opencv/images/08.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

gg = ['/home/k8s/learn_opencv/images/07.jpg','/home/k8s/learn_opencv/images/08.jpg']
# def mouse_click(event, x, y, flags, para):
#         if event == cv2.EVENT_LBUTTONDOWN:  # 左边鼠标点击
#             print('PIX:', x, y)
#             print("BGR:", img[y, x])
#             print("GRAY:", gray[y, x])
#             print("HSV:", hsv[y, x])
cv2.namedWindow('HSV',cv2.WINDOW_NORMAL)
cv2.createTrackbar('upper_H','HSV',0,180,nothing)
cv2.createTrackbar('upper_S','HSV',0,255,nothing)
cv2.createTrackbar('upper_V','HSV',0,255,nothing)
cv2.createTrackbar('lower_H','HSV',0,180,nothing)
cv2.createTrackbar('lower_S','HSV',0,255,nothing)
cv2.createTrackbar('lower_V','HSV',0,255,nothing)
cv2.createTrackbar('area_h','HSV',0,1000,nothing)
cv2.createTrackbar('area_l','HSV',0,1000,nothing)

cv2.createTrackbar('Switch_Pic','HSV',0,1,nothing)

flag = 0
Switch_Pic_last = 0
x,y,w,h =0,0,0,0

class ROI_class:
    def __init__(self):
        self.image_RGB = None
        self.image_HSV = None
        self.image_GREY = None
        self.upper_H = None
        self.upper_S = None
        self.upper_V = None
        self.lower_H = None
        self.lower_S = None
        self.lower_V = None
        self.lower = None
        self.upper = None
        self.mask = None
        self.contours = None
        self.hier = None
        self.area_h = None
        self.area_l = None
(cx, cy), (width, height) = (0,0),(0,0)

while True:
    
    # # lower = np.array([320,40,60])
    # # upper = np.array([330,50,80])
    
    upper_H=cv2.getTrackbarPos('upper_H','HSV')
    upper_S=cv2.getTrackbarPos('upper_S','HSV') 
    upper_V=cv2.getTrackbarPos('upper_V','HSV')
    lower_H=cv2.getTrackbarPos('lower_H','HSV')
    lower_S=cv2.getTrackbarPos('lower_S','HSV')
    lower_V=cv2.getTrackbarPos('lower_V','HSV')
    
    Switch_Pic=cv2.getTrackbarPos('Switch_Pic','HSV')  
    
    
    # img = cv2.imread(gg[Switch_Pic])
    # if Switch_Pic==Switch_Pic_last :
    #     flag = 0
    # else:
    #     flag = 1
    
    # # img = a[Switch_Pic][:,:]
    # # ROI = img
    
    
    # lower_H,lower_S,lower_V = 160,15,130
    # upper_H,upper_S,upper_V = 180,255,255
    
    
    # lower = np.array([lower_H,lower_S,lower_V])
    # upper = np.array([upper_H,upper_S,upper_V])
    
    # # img = cv2.imread('/home/k8s/learn_opencv/images/07.jpg')
    # image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # mask = cv2.inRange(image,lower,upper)
    # # cv2.setMouseCallback("img", mouse_click)
    
    # if 1 == 1:
    #     contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
    #     # x,y,w,h = 0,0,img.shape[0],img.shape[1]
    #     if len(contours)!=0:
    #         for contour in contours:
    #             if cv2.contourArea(contour)>1000:
    #                 x,y,w,h = cv2.boundingRect(contour)
    #                 # cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    #     flag = 0
    # else:
    #     pass
    # # g={}
    # # g[0]=img[0][x:x+w]
    # # g[1]=img[1][y:y+h]
    # # g[2]=img[2]
    # # ROI = image[x:x+w, y:y+h]
    
    # # cv2.imshow("origin",img)
    # # cv2.imshow("image",image)
    # # cv2.imshow("HSV",mask)

    ROI = ROI_class()
    # ROI.image_RGB = img[int(y+h/2):y+h,x:x+w]
    ROI.image_RGB = cv2.imread(gg[Switch_Pic])
    # if h>0 and w>0:
    #     cv2.imshow("clip",ROI)
    # try:
    #     ROI = img[y:y+h,x:x+w]
    #     cv2.imshow("clip",ROI)
    # except:
    #     pass

    ROI.upper_H=cv2.getTrackbarPos('upper_H','HSV')
    ROI.upper_S=cv2.getTrackbarPos('upper_S','HSV') 
    ROI.upper_V=cv2.getTrackbarPos('upper_V','HSV')
    ROI.lower_H=cv2.getTrackbarPos('lower_H','HSV')
    ROI.lower_S=cv2.getTrackbarPos('lower_S','HSV')
    ROI.lower_V=cv2.getTrackbarPos('lower_V','HSV')
    
    ROI.area_h=cv2.getTrackbarPos('area_h','HSV')
    ROI.area_l=cv2.getTrackbarPos('area_l','HSV')
    
    # ROI.lower_H,ROI.lower_S,ROI.lower_V = 100,84,134
    # ROI.upper_H,ROI.upper_S,ROI.upper_V = 150,255,255
    
    ROI.lower = np.array([ROI.lower_H,ROI.lower_S,ROI.lower_V])
    ROI.upper = np.array([ROI.upper_H,ROI.upper_S,ROI.upper_V])
    
    ROI.image_HSV = cv2.cvtColor(ROI.image_RGB,cv2.COLOR_BGR2HSV)
    ROI.mask = cv2.inRange(ROI.image_HSV,ROI.lower,ROI.upper)
    
    cv2.imshow("ROI.mask",ROI.mask)
    
    # 寻找轮廓
    ROI.contours, ROI.hier = cv2.findContours(ROI.mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 声明画布 拷贝自img
    # canvas = np.copy(img)
    Point_list=[]
    img_backup = cv2.imread(gg[Switch_Pic])
    for cidx,cnt in enumerate(ROI.contours):
        ((cx, cy), (width, height), theta) = cv2.minAreaRect(cnt)
        minAreaRect = ((cx, cy), (width, height), theta)
        # 将浮点数坐标转换成整数
        rectCnt = np.int64(cv2.boxPoints(minAreaRect))
            
        rectCnt = np.array([rectCnt[0].tolist(),rectCnt[1].tolist(),rectCnt[2].tolist(),rectCnt[3].tolist()])
        # print(np.array([rectCnt[0].tolist(),rectCnt[1].tolist(),rectCnt[2].tolist(),rectCnt[3].tolist()]))
        print("\n")
        area = width * height
        # 300 1500
        if area >ROI.area_l and area < ROI.area_h and width < 1.5* height and height < 1.5 * width :
            cv2.drawContours(ROI.image_RGB, 
                             [
                                 rectCnt
                                 ], 0, (0,255,0), 3)
            cv2.drawContours(img_backup, [rectCnt], 0, (0,255,0), 3)
            # print((cx, cy), (width, height))
            Point_list.append(rectCnt)
            # print(rectCnt)
    # for cidx,cnt in enumerate(contours):
    #     ((cx, cy), (width, height), theta) = cv2.minAreaRect(cnt)
    #     # print('center: cx=%.3f, cy=%.3f, width=%.3f, height=%.3f, roate_angle=%.3f'%(cx, cy, width, height, theta))
    #     print(cv2.boxPoints(minAreaRect))
    # print("\n") 
    # cv2.imshow("ROI.image_RGB",(ROI.image_RGB))
    # Point_list = Point_list[0]
    # print(Point_list)
    ans=[]
    
    try:
    
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
            ############
            # print(ans)
            ############
            
        if Point_list[1][0][0]>Point_list[0][0][0]:
            
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
            ############
            # print(ans)
    except:
        pass
    
    # print(Point_list)
    import math
    try:
        a = math.pow(ans[0][1]-ans[1][1],2)
        b = math.pow(ans[0][0]-ans[1][0],2)
        r = math.sqrt(a+b)
        r = int(r)
        print([r,ans[0][0],ans[0][1]])
    except:
        pass
    cv2.imshow("origin",img_backup)
    Switch_Pic_last = Switch_Pic

    
    
    if cv2.waitKey(1)==ord(' '):
        break
    #摧毁所有窗口
cv2.destroyAllWindows()
    
    
    