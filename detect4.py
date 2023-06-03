import cv2
import numpy as np
import math
def search(mask):
    x = mask.shape[0]
    y = mask.shape[1]
    for i in range(x - 1, -1, -1):
        for j in range(max(x, y)):
            if i + j >= x or j >= y:
                break
            else:
                if mask[i + j][j] > 0:
                    x0, y0 = j, i + j
                    return x0, y0
                # cv2.circle(mask, (j,i + j), 2, (225, 0, 0), 5)
                # print(mask[i + j][j], end = ' ')
    for i in range(y):
        for j in range(max(x, y)):
            if i + j >= y or j >= x:
                break
            else:
                if mask[i + j][j] > 0:
                    x0, y0 = i + j, j
                    return x0, y0
                # cv2.circle(mask, (i + j,j), 2, (225, 0, 0), 5)
    return 0,0
        #         print(mask[j][i + j], end = ' ')
        # print('\n')


def search_points(mask):
    x = mask.shape[0]
    y = mask.shape[1]
    for i in range(y):
        for j in range(max(x, y)):
            if y - j - 1 < 0 or x - i + j - 1 < 0 or x - i + j - 1 >= x:
                break
            else:
                if mask[x - i + j - 1][y - j - 1] > 0:
                    x1, y1 = y - j - 1, x - i + j - 1
                    return x1, y1
    for i in range(y - 1, -1, -1):
        for j in range(max(x, y)):
            if i - j < 0 or j >= x:
                break
            else:
                if mask[j][i - j] > 0:
                    x1, y1 = i - j, j
                    return x1, y1
    return 0, 0


def detect(readimg):
    img = readimg
    asix2 = img.shape[1]
    # 通过 HSV 对应的绿色色彩区间对绿色部分进行提取
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([105, 69, 87])
    upper = np.array([137, 126, 233])
    mask = cv2.inRange(hsv, lower, upper)
    Imask = cv2.erode(mask, None, iterations=2)  # 腐蚀
    Imask = cv2.dilate(Imask, np.ones((3, 3), np.uint8), iterations=2)  # 膨胀

    # cv2.imshow("腐蚀过后", Imask)
    cv_contours = []
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 10000:
            cv_contours.append(contour)
        else:
            continue
    cv2.fillPoly(mask, cv_contours, (0, 0, 0))
    # cv2.imshow("tiankeng", Imask)

    ################# 找中心点 ####################
    for i in range(asix2):
        if Imask[0][i] > 0:
            # 第一次遇到柱子
            x0 = i
            break
    for i in range(asix2, 0, -1):
        if Imask[0][i - 1] > 0:
            # 第一次遇到柱子
            x1 = i
            break

    mid_line = int(abs(x0 + x1) / 2)
    # 得到中点

    mask_L = Imask[:420, 0:mid_line]
    mask_R = Imask[:420, mid_line:-1]

    # 右边图像
    x0, y0 = search(mask_R)
    ## 转化坐标为标准坐标 (右边点的坐标)
    x0, y0 = x0 + mid_line, y0
    ## 左边点的坐标
    x1, y1 = search_points(mask_L)
    ### 距离R
    r = math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
    return r, x1, y1