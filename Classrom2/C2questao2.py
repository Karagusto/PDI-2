# questão2 (AND, OR, NOT, XOR)
import numpy as np
import cv2

cv2.__version__

img1 = cv2.imread("lena.png")
img2 = cv2.imread("baboon.png")

img_and = cv2.bitwise_and(img2, img1)

cv2.imshow("AND", img_and)
cv2.imshow("OR", cv2.bitwise_or(img2, img1))
cv2.imshow("XOR", cv2.bitwise_xor(img2, img1))
cv2.imshow("NOT", cv2.bitwise_not(img2, img1))
cv2.waitKey(0)
cv2.destroyAllWindows()
