import cv2
import numpy as np


def detect(img):
    # canny 边缘检测
    edge = cv2.Canny(img, 40, 60)

    # 轮廓检测
    contours, _ = cv2.findContours(
        edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 遍历轮廓
    for contour in contours:
        # 矩形拟合
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        x, y, w, h = cv2.boundingRect(contour)

        # 目标筛选
        if 80000 > w * h > 15000:
            box = sorted(box, key=lambda x: x[1])
            line = sorted(box[-2:], key=lambda x: x[0])
            return np.sqrt(np.power(line[0] - line[1], 2).sum()), line[0][0], line[0][1]
    return 0, 0, 0