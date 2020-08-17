import cv2 as cvt
import numpy as np

img = cvt.imread("Karti.jpg")
img = cvt.resize(img, (832, 624))

w, h = 250, 350
pts1 = np.float32([[241, 359], [406, 222], [443, 610], [614, 450]])
pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
matrix = cvt.getPerspectiveTransform(pts1, pts2)
imgOutput = cvt.warpPerspective(img, matrix, (w, h))

cvt.imshow("AA", img)
cvt.imshow("ijsdf", imgOutput)

cvt.waitKey(0)