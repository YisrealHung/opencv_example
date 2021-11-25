import cv2

img = cv2.imread("data/album.jpg")

img1 = cv2.resize(img, (640, 480), interpolation=cv2.INTER_NEAREST)
img2 = cv2.resize(img, (640, 480), interpolation=cv2.INTER_AREA)

cv2.imshow("windows", img1)
cv2.imshow("windows2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

