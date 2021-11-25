import cv2

img = cv2.imread("data/album.jpg")
img = cv2.resize(img, (640, 480))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
canny = cv2.Canny(blur, 30, 150)

cnts, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#cv2.drawContours(img, cnts, -1, (255, 0, 255), 2)
for i in cnts:
    peri = cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, 0.01 * peri, True)
    
    area = cv2.contourArea(i)
    
    if area > 10000:
        cv2.drawContours(img, [approx], -1, (255, 255, 0), 3)
    print(area)

cv2.imshow("canny", canny)
cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

