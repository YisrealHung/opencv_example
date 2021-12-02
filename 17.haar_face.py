import cv2

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    rects = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(30,30))

    for (x, y, w, h) in rects:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 5)


    cv2.imshow("windows", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
