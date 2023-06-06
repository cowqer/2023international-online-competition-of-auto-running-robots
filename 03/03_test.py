import cv2
import numpy as np

local_pic_path = ['../images/05.jpg','../images/06.jpg']

cv2.namedWindow('Canny',cv2.WINDOW_NORMAL)

def nothing(x):
    pass

cv2.createTrackbar('ee','Canny',1,5,nothing)
cv2.createTrackbar('dd','Canny',1,5,nothing)
cv2.createTrackbar('ii','Canny',0,1,nothing)


def detect(img,ee,dd):
    # 转换 HSV 色彩空间
    # ee = 2
    # dd = 5 
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 通过 HSV 对应的绿色色彩区间对绿色部分进行提取
    lower = np.array([50, 43, 46])
    upper = np.array([95, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)


    cv2.imshow("Color",mask)
    # 图像腐蚀 去除一些干扰小区域 只保留最大的绿色板
    # kernel = np.ones((5, 5), np.uint8)
    # mask = cv2.erode(mask, kernel, iterations=ee)
    
    kernel = np.ones((3, 3), dtype=np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=ee)
    
    kernel = np.ones((3, 3), dtype=np.uint8)
    mask = cv2.dilate(erosion, kernel, iterations=dd) # 1:迭代次数，也就是执行几次膨胀操作
    
    cv2.imshow("Mask",mask)

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

while(1):
    
    #返回当前阈值
    # img_output = img
    # threshold1=cv2.getTrackbarPos('threshold1','Canny')
    # threshold2=cv2.getTrackbarPos('threshold2','Canny')
    # param1=cv2.getTrackbarPos('param1','Canny')
    # param2=cv2.getTrackbarPos('param2','Canny')
    # a=cv2.getTrackbarPos('a','Canny')
    # b=cv2.getTrackbarPos('b','Canny')
    # minRadius = cv2.getTrackbarPos('minRadius','Canny')
    # maxRadius = cv2.getTrackbarPos('maxRadius','Canny')
    
    # dd = cv2.getTrackbarPos('dd','Canny')
    # ee = cv2.getTrackbarPos('ee','Canny')
    # ii = cv2.getTrackbarPos('ii','Canny')
    # img_output=cv2.Canny(img,threshold1,threshold2)

    #显示图片
    # r, x, y = (int(x) for x in detect(img,threshold1,threshold2))

    # 绘制结果
    ee = cv2.getTrackbarPos('ee','Canny')
    dd = cv2.getTrackbarPos('dd','Canny')
    ii = cv2.getTrackbarPos('ii','Canny')

    img = cv2.imread(local_pic_path[ii])
    
    output_img = img.copy()
   
        
    r, x, y = (int(x) for x in detect(output_img,ee,dd))
        
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
