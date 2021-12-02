import cv2
import time
import numpy as np

H_min = 0
H_max = 0
S_min = 0
S_max = 0
V_min = 0
V_max = 0

lower_bound = np.array([H_min, S_min, V_min])
upper_bound = np.array([H_max, S_max, V_max])

cap = cv2.VideoCapture(0)

time.sleep(2)
_, background = cap.read()


while True:
    _, img = cap.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #mask = cv2.inRange(hsv, lower_bound, upper_bound)

    #cloak = cv2.bitwise_and(background, background, mask=mask)

    #inverse_mask = cv2.bitwise_not(mask)

    #current_background = cv2.bitwise_and(img, img, mask=inverse_mask)

    #combined = cv2.add(cloak, current_background)

    cv2.imshow("win1", img)
    cv2.imshow("win2", hsv)


    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
