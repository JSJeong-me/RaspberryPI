# -*- coding: utf-8 -*-
"""cv2_03-shv-banana-1025.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/JSJeong-me/KOSA_Vision_Exercise/blob/main/cv2_03_shv_banana_1028.ipynb
"""

import cv2
import numpy as np
#from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt

src1 = cv2.imread('./banana3.png')

src2 = cv2.cvtColor(src1, cv2.COLOR_BGR2HSV)

"""69 81 130
255 255 255   # Green

19 0 237 255 255 255  # Yellow  

0  185 215
255 255 255   # Red

"""

# 21 39 183 low H S V
# 255 255 255 High H S V

low_green = np.array([66, 80, 125])
high_green = np.array([255, 255, 255])

low_yellow = np.array([19, 37, 181])
high_yellow = np.array([255, 255, 255])

low_red = np.array([0, 183, 213])
high_red = np.array([255, 255, 255])

#mask = cv2.inRange(src2, low_green, high_green)
mask = cv2.inRange(src2, low_yellow, high_yellow)
#mask = cv2.inRange(src2, low_red, high_red)

src1_sub = cv2.bitwise_and(src2, src2, mask = mask)

cv2.imshow('Original', src1)
cv2.imshow('Masked', mask)
cv2.imshow('Substracted', src1_sub)

ret, thr = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Threshold', thr)
print(ret)

blur = cv2.medianBlur(thr,3)

cv2.imshow('Blurred', blur)

cnts, _ = cv2.findContours(blur.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(len(cnts))

copy2 = blur.copy()
count = []
for x in cnts:
    area = cv2.contourArea(x)
    if area > 100:
        count.append(x)
cv2.drawContours(src1, count, -1, (0,255,0), 3)
cv2.imshow('Src', src1)
print("number of lemons found via contour detection = ", len(count))

for x in cnts:
  area +=cv2.contourArea(x)

print(area)


cv2.waitKey(0)

cv2.destroyAllWindows()