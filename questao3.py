import numpy as np
import cv2

lena_original = cv2.imread("lena.png")
# img_black = np.zeros((lena_original.shape[0], lena_original.shape[0], 3), dtype=np.uint8)
# img_white = np.zeros((lena_original.shape[0], lena_original.shape[0], 3), dtype=np.uint8)
#
# img_white[:, :, 0] = 255
# img_white[:, :, 1] = 255
# img_white[:, :, 2] = 255
#
# lena_dark = cv2.addWeighted(lena_original, 0.7, img_black, 0.3, 0)
# lena_bright = cv2.addWeighted(lena_original, 0.7, img_white, 0.3, 0)
#
# cv2.imshow("image", lena_dark)
# cv2.imshow("image2", lena_original)
# cv2.imshow("image3", lena_bright)
#
# cv2.waitKey()

x = 1
y = 100


lena_bright = np.zeros((lena_original.shape[0], lena_original.shape[0], 3), dtype=np.uint8)
lena_dark = np.zeros((lena_original.shape[0], lena_original.shape[0], 3), dtype=np.uint8)


for i in range(lena_original.shape[0]):
    for j in range(lena_original.shape[1]):
        for k in range(lena_original.shape[2]):
            lena_bright[i,j,k] = np.clip(x*lena_original[i,j,k] + y, 0, 255)
            lena_dark[i,j,k] = np.clip(x*lena_original[i,j,k] - y, 0, 255)
cv2.imshow("lena_bright", lena_bright)
cv2.imshow("lena_original", lena_original)
cv2.imshow("lena_dark", lena_dark)

cv2.waitKey()