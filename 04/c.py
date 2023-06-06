import cv2
import numpy as np

img = cv2.imread('/home/k8s/learn_opencv/images/07.jpg')

# range of red
lower_red = np.array([160, 60, 60])
upper_red = np.array([180, 255, 255])

lower_red2 = np.array([0, 60, 60])
upper_red2 = np.array([10, 255, 255])  # thers is two ranges of red

# range of yellow
# lower_yellow = np.array([10,100,100])
# upper_yellow = np.array([45,255,255])

# range of grenn
# lower_yellow = np.array([36,25,25])
# upper_yellow = np.array([70,255,255])

# change to hsv model
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask_r = cv2.inRange(hsv, lower_red, upper_red)

mask_r2 = cv2.inRange(hsv, lower_red2, upper_red2)

mask = mask_r + mask_r2

cv2.namedWindow('Mask', 0)
cv2.imshow('Mask', mask)
cv2.waitKey()

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
mask = cv2.dilate(mask, kernel)

cv2.namedWindow('Mask_dilate', 0)
cv2.imshow('Mask_dilate', mask)
cv2.waitKey()

# 将mask于原视频帧进行按位与操作，则会把mask中的白色用真实的图像替换：
res = cv2.bitwise_and(img, img, mask=mask)

cv2.namedWindow('res', 0)
cv2.imshow('res', res)
cv2.waitKey()


