import math

def getAreaMaxContour(contours):
    contour_area_temp = 0
    contour_area_max = 0
    area_max_contour = None
    for c in contours:
        contour_area_temp = math.fabs(cv.contourArea(c))
        if contour_area_temp > contour_area_max:
            contour_area_max = contour_area_temp
            if contour_area_temp > 25:  # 轮廓面积大于25时最大轮廓才有效
                area_max_contour = c
    return area_max_contour, contour_area_max

def getAreaMaxContour2(contours, contour_area_max):
    contour_area_temp = 0
    contour_area_max2 = 0
    area_max_contour2 = None
    for c in contours:
        contour_area_temp = math.fabs(cv.contourArea(c))
        if contour_area_temp > contour_area_max2 and contour_area_max != contour_area_temp:
            contour_area_max2 = contour_area_temp
            if contour_area_temp > 25:  # 轮廓面积大于25时最大轮廓才有效
                area_max_contour2 = c
    return area_max_contour2, contour_area_max2


def detect(readimg):

    color_range = {'blue_door': [(94, 64, 75), (146, 217, 224)],}

    #border = cv.copyMakeBorder(readimg, 12, 12, 16, 16, borderType=cv2.BORDER_CONSTANT,
    #                                value=(255, 255, 255))  # 扩展白边，防止边界无法识别
    frame_gauss = cv.GaussianBlur(readimg, (3, 3), 0)  # 高斯模糊
    frame_hsv = cv.cvtColor(frame_gauss, cv.COLOR_BGR2HSV)  # 将图片转换到HSV空间
    frame_green = cv.inRange(frame_hsv, color_range['blue_door'][0], color_range['blue_door'][1])  # 对原图像和掩模(颜色的字典)进行位运算
    opened = cv.morphologyEx(frame_green, cv.MORPH_OPEN, np.ones((3, 3), np.uint8))  # 开运算 去噪点
    closed = cv.morphologyEx(opened, cv.MORPH_CLOSE, np.ones((3, 3), np.uint8))  # 闭运算 封闭连接
    (contours, hierarchy) = cv.findContours(closed, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)  # 找出轮廓cv2.CHAIN_APPROX_NONE
    areaMaxContour, area_max = getAreaMaxContour(contours)  # 找出最大轮廓
    areaMaxContour2, area_max2 = getAreaMaxContour2(contours,area_max)
    
    #cv.imshow('closed', closed)  # 显示图像
    #cv.drawContours(readimg, contours, -1, (255, 0, 255), 3)
    #time.sleep(4)
    cv.imwrite("result.png", closed)
    
    if areaMaxContour is not None:
        btm1 = areaMaxContour[0][0]
        for c in areaMaxContour:
            if (c[0][1]) > (btm1[1]):
                btm1 = c[0]
    if areaMaxContour2 is not None:
        btm2 = areaMaxContour2[0][0]
        for d in areaMaxContour2:
            if (d[0][1]) > (btm2[1]):
                btm2 = d[0]

    if btm1[0] < btm2[0]:
        x = btm1[0]
        y = btm1[1]
        x1 = btm2[0]
        y1 = btm2[1]
    else:
        x = btm2[0]
        y = btm2[1]
        x1 = btm1[0]
        y1 = btm1[1]
    r = math.sqrt((btm2[0]-btm1[0])*(btm2[0]-btm1[0]) + (btm2[1]-btm1[1])*(btm2[1]-btm1[1]))
    return r,x,y