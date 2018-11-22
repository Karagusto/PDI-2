import numpy as np
import cv2


imgBlack = np.zeros([400, 400, 3])
cv2.imwrite('black_img.jpg', imgBlack)


imgGray = np.zeros((400, 400, 3), dtype=np.uint8)
imgGray[:, :, 0] = 128
imgGray[:, :, 1] = 128
imgGray[:, :, 2] = 128

cv2.imwrite('gray_img.jpg', imgGray)
cv2.imshow("image", imgBlack)
cv2.imshow("image2", imgGray)
cv2.waitKey()
