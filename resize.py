import cv2
import numpy as np

img = cv2.imread("Karti.jpg")
print(img.shape)

imgRe = cv2.resize(img, (832, 624))
print(imgRe.shape)

imgCrop = img[0:100, 0:100]

#cv2.imshow("image", img)
cv2.imshow("image2", imgRe)
cv2.imshow("Img3", imgCrop)

cv2.waitKey(0)