import cv2

img = cv2.imread("data/box.jpg")
print(img.shape)

cv2.imshow("windows", img)

img[:,:,0] = 0
img[:,:,1] = 0
img[:,:,2] = 0

cv2.imshow("choose", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

