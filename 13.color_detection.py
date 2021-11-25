import cv2
import numpy as np

img = cv2.imread("data/colorbox.jpg")
img = cv2.resize(img, (640, 480))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


lower_blue = np.array([90,80,0])
upper_blue = np.array([115,255,255])


mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

res_blue = cv2.bitwise_and(img,img, mask= mask_blue)

cv2.imshow('frame', img)
cv2.imshow('mask_blue', mask_blue)
cv2.imshow('res_blue', res_blue)


cv2.waitKey(0)

cv2.destroyAllWindows()
