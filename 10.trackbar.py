import cv2

cv2.namedWindow('image')


def change_value(x):
    l_value = cv2.getTrackbarPos('L', 'image')
    h_value = cv2.getTrackbarPos('H', 'image')
    
    canny = cv2.Canny(blur, l_value, h_value)
    cv2.imshow("image", canny)
    
img = cv2.imread("data/album.jpg")
img = cv2.resize(img, (640, 480))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)

cv2.createTrackbar('L', 'image', 0, 255, change_value)
cv2.createTrackbar('H', 'image', 0, 255, change_value)
cv2.setTrackbarPos('L', 'image', 30)
cv2.setTrackbarPos('H', 'image', 150)


cv2.waitKey(0)
cv2.destroyAllWindows()

