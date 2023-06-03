import cv2
import numpy as np

# 定义滑动条回调函数
def nothing(x):
    pass

# 定义检测函数
def detect(img):
    # 灰度化和高斯模糊
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # 使用HoughCircles函数进行霍夫圆检测
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=55, 
                               param2=40, 
                               minRadius=85,
                               maxRadius=122)
    if circles is None:
        return 0, 0, 0
    else:
        return circles[0, 0, 2], circles[0, 0, 0], circles[0, 0, 1]

    return output

# 读取图片并进行处理
img = cv2.imread('../images/1.png')
img2 = cv2.imread('../images/1.png')


output = detect(img)

while True:

    output = detect(img)
    cv2.imshow('image1', output)
    cv2.imshow('image',img2)

    #cv2.imwrite('/home/cq/1.jpg', output)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
