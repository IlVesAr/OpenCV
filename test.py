import cv2
import numpy as np

cap = cv2.VideoCapture(0)
kernel = np.ones((5, 5), np.uint8)
while True:
    s, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgCanny = cv2.Canny(img, 100, 100)
    imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

    cv2.imshow("Gl", img)
    cv2.imshow("Gr", imgGray)
    cv2.imshow("Cn", imgCanny)
    cv2.imshow("Ba", imgDialation)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
