import numpy as np
import cv2


baboon_Img = cv2.imread("baboon.png")
crop_baboon = np.zeros((baboon_Img.shape[0], baboon_Img.shape[1], 3), dtype=np.uint8)

for i in range(baboon_Img.shape[0]):
    if i >= (256) and i <= (480):
        for j in range(baboon_Img.shape[1]):
            if j >= (128) and j <= (352):
                crop_baboon[i,j] = crop_baboon[i,j] + baboon_Img[i,j]


crop_baboon = crop_baboon[256:480, 128:352]
cv2.imshow("image", crop_baboon)

cv2.waitKey()