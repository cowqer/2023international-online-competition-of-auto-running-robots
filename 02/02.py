import cv2
import numpy as np
import sys
import os

# img = cv2.imread('/home/k8s/learn_opencv/images/01.jpg')
# img = cv2.imread('/home/k8s/learn_opencv/images/03.jpg')

local_pic_path = ['../images/03.jpg','../images/04.jpg']

#创建窗口
size = img.shape
w = size[1] #宽度
h = size[0] #高度
# print(w,h)
cv2.namedWindow('Canny',cv2.WINDOW_NORMAL)
cv2.namedWindow('Canny_2',cv2.WINDOW_NORMAL)
# cv2.namedWindow('Canny')
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
# img = cv2.resize(img, (600, 450))
# cv2.resizeWindow("canny", 50, 50)


#定义回调函数
def nothing(x):
    pass

#创建滑动条，分别对应Canny的两个阈值
cv2.createTrackbar('wh','Canny',0,2000,nothing)
cv2.createTrackbar('threshold1','Canny',0,500,nothing)
cv2.createTrackbar('threshold2','Canny',0,500,nothing)
# cv2.createTrackbar('param1','Canny',0,255,nothing)
# cv2.createTrackbar('param2','Canny',0,255,nothing)
# cv2.createTrackbar('a','Canny',0,255,nothing)
# cv2.createTrackbar('b','Canny',0,255,nothing)
# cv2.createTrackbar('minRadius','Canny',0,255,nothing)
# cv2.createTrackbar('maxRadius','Canny',0,255,nothing)
cv2.createTrackbar('ii','Canny',0,1,nothing)

def detect(readimg,Canny1,Canny2):
    
    image = cv2.cvtColor(readimg,cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    edge = cv2.Canny(thresh,Canny1,Canny2) #30 200
    cont = cv2.findContours(edge,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    
    return cont

while(1):
    
    #返回当前阈值
    # img_output = img
    threshold1=cv2.getTrackbarPos('threshold1','Canny')
    threshold2=cv2.getTrackbarPos('threshold2','Canny')
    # param1=cv2.getTrackbarPos('param1','Canny')
    # param2=cv2.getTrackbarPos('param2','Canny')
    # a=cv2.getTrackbarPos('a','Canny')
    # b=cv2.getTrackbarPos('b','Canny')
    # minRadius = cv2.getTrackbarPos('minRadius','Canny')
    # maxRadius = cv2.getTrackbarPos('maxRadius','Canny')
    # img_output=cv2.Canny(img,threshold1,threshold2)
    wh = cv2.getTrackbarPos('wh','Canny')

    #显示图片
    # r, x, y = (int(x) for x in detect(img,threshold1,threshold2))

    # 绘制结果
    ii = cv2.getTrackbarPos('ii','Canny')

    img = cv2.imread(local_pic_path[ii])
    
    output_img = img.copy()
        # output_img_2 = img_2.copy()
        
    # cont = (int(g) for g in detect(img,threshold1,threshold2))
    cont = detect(img,threshold1,threshold2)
    for j,i in enumerate(cont):
        x,y,w,h = cv2.boundingRect(i)

        if (w*h>wh):
            cv2.drawContours(output_img,[i],0,(0,0,255),3)
 

        # cv2.circle(output_img, (x, y), 3, (225, 0, 0), 5)
        # cv2.circle(output_img, (x, y), r, (225, 0, 0), 3)

        
    cv2.imshow('Canny',output_img)
    cv2.imshow('Canny_2',cv2.Canny(img, threshold1,threshold2))
        # concatanate image Horizontally

        # cv2.imshow('Canny',output_img_2)
    #空格跳出
    if cv2.waitKey(1)==ord(' '):
        break

    #摧毁所有窗口
cv2.destroyAllWindows()


