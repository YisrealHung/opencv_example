import cv2

img = cv2.imread("data/album.jpg")

img = cv2.resize(img, (640, 480))

cv2.imshow("windows", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

