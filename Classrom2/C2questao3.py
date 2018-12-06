# questão 3()
import numpy as np
import cv2


img1 = cv2.imread("lena.png")
img2 = cv2.imread("baboon.png")

lena_gray = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
baboon_gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

and_gray = cv2.bitwise_and(lena_gray, baboon_gray)

cv2.imshow("and_gray", and_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
