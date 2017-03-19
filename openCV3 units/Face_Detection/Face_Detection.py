import cv2

"""
Frontalface_Detection
define face_cascade as a CascadeClassifier Class
the pic wating for detected should be a gray picture.
face_cascade.detectMultiScale(src, scaleFactor, minNeighbors)
"""

filename = "Viking.jpg"

def detect(filename):
    face_cascade = cv2.CascadeClassifier("./cascades/haarcascade_frontalface_default.xml")

    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.namedWindow("Wiking Detected!!")
    cv2.imshow("Viking Detected!!", img)
    cv2.waitKey(0)

detect(filename)