import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cv2.namedWindow('image')

lower_blue = np.array([0 ,0, 0])
upper_blue = np.array([0, 0, 0])


def change_value(x):
    global lower_blue, upper_blue
    lh = cv2.getTrackbarPos('H-min', 'image')
    ls = cv2.getTrackbarPos('S-min', 'image')
    lv = cv2.getTrackbarPos('V-min', 'image')
    hh = cv2.getTrackbarPos('H-max', 'image')
    hs = cv2.getTrackbarPos('S-max', 'image')
    hv = cv2.getTrackbarPos('V-max', 'image')
    
    lower_blue = np.array([lh,ls,lv])
    upper_blue = np.array([hh,hs,hv])
    

cv2.createTrackbar('H-min', 'image', 0, 179, change_value)
cv2.createTrackbar('H-max', 'image', 0, 179, change_value)
cv2.createTrackbar('S-min', 'image', 0, 255, change_value)
cv2.createTrackbar('S-max', 'image', 0, 255, change_value)
cv2.createTrackbar('V-min', 'image', 0, 255, change_value)
cv2.createTrackbar('V-max', 'image', 0, 255, change_value)

while True:
    _, img = cap.read()
    #img = cv2.resize(img, (640, 480))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    cv2.imshow('image', mask_blue)

    if cv2.waitKey(1) == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()

