import cv2
import numpy as np

def detect(readimg):

    hsv = cv2.cvtColor(readimg, cv2.COLOR_BGR2HSV)
    #自适应阈值 灵敏度
    sensitivity = 30
    lower = np.array([60 - sensitivity, 100, 50])
    upper = np.array([60 + sensitivity, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)

    # 降噪
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # 轮廓检测
    contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 找最大的
    if len(contours) > 0:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        return w, x, y + h
    else:
        return 0, 0, 0

