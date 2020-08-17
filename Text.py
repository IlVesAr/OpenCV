import cv2 as cvt
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img)

img[101:101, 101:101] = 255, 0, 0

cvt.line(img, (0, 0), (300, 300), (0, 255, 0), 3)
cvt.putText(img, " Texta mi ", (300, 100), cvt.FONT_ITALIC, 1, (255, 0, 0), 4)

cvt.imshow("aaa", img)

cvt.waitKey(0)