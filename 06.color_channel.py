import cv2

img = cv2.imread("data/box.png")
print(img.shape)

cv2.imshow("windows", img)

'''
img[:,:,0]
img[:,:,1]
img[:,:,2]
'''

cv2.imshow("Blue", img[:,:,0])
cv2.imshow("Green", img[:,:,1])
cv2.imshow("Red", img[:,:,2])


cv2.waitKey(0)
cv2.destroyAllWindows()

