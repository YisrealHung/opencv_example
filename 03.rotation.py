import cv2

img = cv2.imread("data/album.jpg")

img = cv2.resize(img, (640, 480))
M = cv2.getRotationMatrix2D((320, 240), 15, 1) #中心座標, 旋轉角度, 縮放比例
rotate = cv2.warpAffine(img, M, (640,480))

cv2.imshow("windows", img)
cv2.imshow("windows2", rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()

