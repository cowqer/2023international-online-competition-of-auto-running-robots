import cv2
import numpy as np

# 定义滑动条回调函数
def nothing(x):
    pass

# 定义检测函数
def detect(img):
    # 灰度化和高斯模糊
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)  # 可以调整核的大小和形状
    eroded_image = cv2.erode(binary_image, kernel, iterations=2)  
    dilated_image = cv2.dilate(eroded_image, kernel, iterations=3)
    # 创建拉普拉斯滤波器
    kernel0 = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]], dtype=np.float32)

# 应用滤波器进行图像锐化
    dilated_image = cv2.filter2D(dilated_image, -1, kernel0)

    # 使用HoughCircles函数进行霍夫圆检测
    circles = cv2.HoughCircles(dilated_image, cv2.HOUGH_GRADIENT, 1, 100,
                               param1=params['param1'], 
                               param2=params['param2'], 
                               minRadius=params['min_radius'],
                               maxRadius=params['max_radius'])
    # 打印出圆的信息
    cv2.imshow('binary_image',binary_image)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            print("圆心坐标：({}, {})，半径：{}".format(x, y, r))

    # 在原图上画出检测到的圆
    output = img.copy()
    if circles is not None:
        for (x, y, r) in circles:
            cv2.circle(output, (x, y), r, (0, 255, 0), 2)

    return output

# 创建窗口和滑动条
cv2.namedWindow('image')
cv2.createTrackbar('param1', 'image', 45, 150, nothing)
cv2.createTrackbar('param2', 'image', 30, 100, nothing)
cv2.createTrackbar('min_radius', 'image', 100, 200, nothing)
cv2.createTrackbar('max_radius', 'image', 100, 300, nothing)

# 初始化参数
params = {'param1': 50, 'param2': 30, 'min_radius': 50, 'max_radius': 200}

# 读取图片并进行处理
img = cv2.imread('../images/3.png')
img2 = cv2.imread('../images/1.png')

#调整图像大小




output = detect(img)

while True:
    # 获取滑动条的值
    params['param1'] = cv2.getTrackbarPos('param1', 'image')
    params['param2'] = cv2.getTrackbarPos('param2', 'image')
    params['min_radius'] = cv2.getTrackbarPos('min_radius', 'image')
    params['max_radius'] = cv2.getTrackbarPos('max_radius', 'image')

    # 在每次循环中重新检测圆并显示结果
    output = detect(img)
    cv2.imshow('image1', output)
    cv2.imshow('image',img2)

    #cv2.imwrite('/home/cq/1.jpg', output)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
