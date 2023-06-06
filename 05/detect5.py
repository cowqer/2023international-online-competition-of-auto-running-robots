import cv2
import numpy as np

def detect(readimg):
    Canny1,Canny2 = 500,235
    param1,param2 = 1,16
    a,b=0,0
    minRadius,maxRadius = 0,26
    dd,ee=4,3
    
    
    kernel = np.ones((3, 3), dtype=np.uint8)
    erosion = cv2.erode(readimg.copy(), kernel, iterations=ee)
    
    kernel = np.ones((3, 3), dtype=np.uint8)
    dilate = cv2.dilate(erosion, kernel, iterations=dd) # 1:迭代次数，也就是执行几次膨胀操作
    
    # try:
    canny = cv2.Canny(dilate, Canny1, Canny2)
    
    # cv2.imshow("canny", canny)
    # 圆形检测
    circles = cv2.HoughCircles(
        canny, cv2.HOUGH_GRADIENT, 1, 30, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

    if circles is None:
        return 0, 0, 0
    else:
        return circles[0, 0, 2], circles[0, 0, 0], circles[0, 0, 1]
    # except:
    #     return 0, 0, 0
