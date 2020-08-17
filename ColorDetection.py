import cv2 as cvt
import numpy as np


def empty():
    pass


cvt.namedWindow("TrackBars")
cvt.resizeWindow("TrackBars", 640, 240)
cvt.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cvt.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cvt.createTrackbar("Sat Min", "TrackBars", 116, 255, empty)
cvt.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cvt.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cvt.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    img = cvt.imread('Karti.jpg')
    img = cvt.resize(img, (832, 624))

    imgHSV = cvt.cvtColor(img, cvt.COLOR_BGR2HSV)
    h_min = cvt.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cvt.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cvt.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cvt.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cvt.getTrackbarPos("Val Min", "TrackBars")
    v_max = cvt.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cvt.inRange(imgHSV, lower, upper)
    imgResult = cvt.bitwise_and(img, img, mask=mask)

    cvt.imshow("aaa", img)
    cvt.imshow("aaaa", imgHSV)
    cvt.imshow("Mask", mask)
    cvt.imshow("res", imgResult)
    cvt.waitKey(1)