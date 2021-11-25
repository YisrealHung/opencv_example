import cv2
    
img = cv2.imread("data/album.jpg")
img = cv2.resize(img, (640, 480))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
canny = cv2.Canny(blur, 30, 150)

cv2.imshow("windows", img)
cv2.imshow("gray", gray)
cv2.imshow("blur", blur)
cv2.imshow("canny", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()

