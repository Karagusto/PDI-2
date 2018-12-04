# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:57:55 2018

@author: @karagusto
"""

#%%

"""

normalizedImg = np.zeros((800, 800))
normalizedImg1 = cv2.normalize(img1,  normalizedImg, 0, 255, cv2.NORM_MINMAX)
normalizedImg2 = cv2.normalize(img2,  normalizedImg, 0, 255, cv2.NORM_MINMAX)

dst = cv2.add(img1,img2)
for i in range(img1.shape[0])
dst = cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('dst',dst)

"""
import numpy as np
import matplotlib.pyplot as plt
import cv2

cv2.__version__

cv2.namedWindow('img', cv2.WINDOW_KEEPRATIO)

a = 0.5
b = 0.2
img1 = cv2.imread('lena.png')
img2 = cv2.imread('baboon.png')

img1_1 = img1.astype('float')
img2_2 = img2.astype('float')
"""

"""
dst = a*img1_1 + b*img2_2

diff = a*img1_1 - b*img2_2

maxi = np.zeros((img1.shape[0], img1.shape[0], 3), dtype=np.uint8)
cv2.max(img1, img2, maxi)

dst = dst/255
diff = diff/255

height, width = img1.shape[:2]
res = cv2.resize(img1,(width, height/2), interpolation = cv2.INTER_CUBIC)

rows = 512
cols = 512

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
rot = cv2.warpAffine(img1,M,(cols,rows))


cv2.imshow('sum', dst)
cv2.imshow('max', maxi)
cv2.imshow('diff', diff)
cv2.imshow('stretch', res)
cv2.imshow('rot', rot)





cv2.waitKey(0)
cv2.destroyAllWindows()


