# -*-coding:utf-8-*-

import cv2
import numpy as np

"""
通过HoughLines和HoughLinesP函数完成检测
HoughLinesP(概率)是对HoughLines(标准)的油画，通过分析点的子集估计在一条直线的概率
"""

img = cv2.imread("hi.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 120)
minLineLength = 20
maxLineGap = 5
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow("edges", edges)
cv2.imshow("lines", lines)
cv2.waitKey()
cv2.destroyAllWindows()