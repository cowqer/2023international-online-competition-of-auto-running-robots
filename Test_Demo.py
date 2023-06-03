#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2 as cv
import numpy as np
import os
import pandas as pd
import csv
import timeit
import imutils
import json
import base64
from itertools import islice
#import requests



##########以下detect函数是应提交的识别程序##########

def detect(readimg):
    '''
    根据要求识别图片中的物品：如小球、横杆、坑洞等。
    :param readimg:
    :return:
    '''
    ###以下代码以第一关：识别小球示例#####
    gray = cv.cvtColor(readimg, cv.COLOR_BGR2GRAY)
    gray = cv.bilateralFilter(gray, 21, 75, 75)
    # gray = cv.medianBlur(gray, 7)
    gray = cv.convertScaleAbs(cv.Laplacian(gray, cv.CV_64F))
    edges = cv.Canny(gray, 50, 150)
    circles = cv.HoughCircles(edges,cv.HOUGH_GRADIENT, 1, 120, param1=100, param2=30, minRadius=0, maxRadius=0)

    if np.any(circles!=None):
        circles = np.uint16(np.around(circles))
    else:
        circles=np.array([[[0,0,0]]])

    choose=circles[0,:]

    r,x,y = (choose[0, 2]), (choose[0, 0]), (choose[0, 1])
    return r,x,y
###请各位各显神通！最终提交各个关卡的detect（readimg）函数即可!!!######

if __name__ == '__main__':
    '''
    主程序入口
    '''
    start = timeit.default_timer()
    if (os.path.exists("result_data.csv")):
        os.remove("result_data.csv")
        print("Deleting result_data.csv!")
    else:
        print("重建 result_data.csv!")

    # 新建文件result_data.csv，并写入列头
    with open("result_data.csv", 'w', newline='', encoding='utf-8-sig') as resultfile:
        header = ['num', 'ball_r', 'ball_x', 'ball_y']
        csv_write = csv.writer(resultfile)
        csv_write.writerow(header)

        readpath = "./pictures/"  ##定义图片库路径
        readfiles = sorted(os.listdir(readpath))  # 获取图片
        num = 0
        for readfile in readfiles:
            num += 1
            readposition = readpath + '/' + readfile  # 图片文件路径
            readimg = cv.imread(readposition)
            end = timeit.default_timer()
            runtime = end - start
            # print(str(runtime),end,start)
            if runtime > 600:
                print("运行超时", runtime)
                exit()
            r, x, y = detect(readimg)
            data_row = [num, r, x, y]
            csv_write.writerow(data_row)

    ##
    print("End:result_data已生成!", runtime)
