import cv2
import numpy as np

cv2.namedWindow('image')

img = cv2.imread("data/colorbox.jpg")
img = cv2.resize(img, (640, 480))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def change_value(x):
    lh = cv2.getTrackbarPos('lh', 'image')
    ls = cv2.getTrackbarPos('ls', 'image')
    lv = cv2.getTrackbarPos('lv', 'image')
    hh = cv2.getTrackbarPos('hh', 'image')
    hs = cv2.getTrackbarPos('hs', 'image')
    hv = cv2.getTrackbarPos('hv', 'image')
    
    lower_blue = np.array([lh,ls,lv])
    upper_blue = np.array([hh,hs,hv])
    
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    cv2.imshow('image', mask_blue)

cv2.createTrackbar('lh', 'image', 0, 179, change_value)
cv2.createTrackbar('ls', 'image', 0, 255, change_value)
cv2.createTrackbar('lv', 'image', 0, 255, change_value)
cv2.createTrackbar('hh', 'image', 0, 179, change_value)
cv2.createTrackbar('hs', 'image', 0, 255, change_value)
cv2.createTrackbar('hv', 'image', 0, 255, change_value)

cv2.waitKey(0)

cv2.destroyAllWindows()
