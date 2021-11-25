import cv2

img = cv2.imread("data/album.jpg")
img = cv2.resize(img, (640, 480))

x1 = 282
y1 = 140
x2 = 386
y2 = 366

cut = img[y1:y2, x1:x2]

cv2.imshow("windows", img)
cv2.imshow("windows2", cut)

cv2.imwrite("new.jpg", cut)

cv2.waitKey(0)
cv2.destroyAllWindows()

