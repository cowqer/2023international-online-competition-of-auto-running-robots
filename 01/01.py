# -*- coding: utf-8 -*- 
'''
    可视化颜色阈值调参软件
'''

import cv2
import numpy as np
import sys
import os

def test():
    # # 获取路径
    # img_path = os.path.join('images', img_name)
    img_path = '/home/k8s/learn_opencv/images/01.jpg'
    # 读取图像
    img = cv2.imread(img_path)
    Canny1 = cv2.getTrackbarPos('Canny1','image')
    Canny2 = cv2.getTrackbarPos('Canny2','image')
    print('更新阈值')
    print(Canny1)
    print(Canny2)
    # 图像检测
    r, x, y = (int(x) for x in detect(img,Canny1,Canny2))

    # 绘制结果
    cv2.circle(img, (x, y), 3, (225, 0, 0), 5)
    cv2.circle(img, (x, y), r, (225, 0, 0), 3)
    cv2.imshow('mask',img)

def detect(readimg,Canny1,Canny2):
    # Canny 边缘检测
    
    canny = cv2.Canny(readimg, Canny1,Canny2)

    # 圆形检测
    circles = cv2.HoughCircles(
        canny, cv2.HOUGH_GRADIENT, 1, 30, param1=50, param2=30, minRadius=80, maxRadius=900)
    
    if circles is None:
        return 0, 0, 0
    else:
        return circles[0, 0, 2], circles[0, 0, 0], circles[0, 0, 1]

def main(img):
    
    cv2.namedWindow('image', flags= cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)


    cv2.createTrackbar('Canny1','image',0,255)
    cv2.createTrackbar('Canny2','image',0,255)
    cv2.setTrackbarPos('Canny1', 'image', 255)
    cv2.setTrackbarPos('Canny1', 'image', 0)
   
    test()
    print("调试棋子的颜色阈值, 键盘摁e退出程序")
    while cv2.waitKey(0) != ord('e'):
        continue

    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 样例图片 (从命令行中填入)
    image_path = sys.argv[1]
    # 样例图片 (在代码中填入)
    # img = cv2.imread('cfs_samples.jpg')
    img = cv2.imread(image_path)
    if img is None:
        print("Error: 文件路径错误，没有此图片 {}".format(image_path))
        exit(1)

    main(img)