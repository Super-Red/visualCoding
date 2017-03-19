# -*-coding:utf-8 -*-

import cv2
import numpy as np

"""
Canny函数一行就能识别出边缘
算法非常复杂，用了5个步骤
A.高斯滤波器去燥 B.计算梯度 C.边缘上使用非最大抑制(NMS) 
D.检测到的边缘上用双阀值去除假阳性 
E.分析所有边缘及期间连接以保留真正边缘，消除不明显边缘
"""

img = cv2.imread("hi.jpg", 0)
cv2.imwrite("canny.jpg", cv2.Canny(img, 200, 300))
cv2.imshow("canny", cv2.imread("canny.jpg"))
cv2.waitKey()
cv2.destroyAllWindows()