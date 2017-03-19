import cv2

"""
Frontalface_Detection
define face_cascade as a CascadeClassifier Class
the pic wating for detected should be a gray picture.
face_cascade.detectMultiScale(src, scaleFactor, minNeighbors)

we can detect the eyes just in the area selected by face_detection.
two more parameters in the eye_detection because the shadow from the nose of bread 
or the random shadow will produce a false positive, thus the search scale should be minimized
"""


def detect():
    face_cascade = cv2.CascadeClassifier("./cascades/haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier("./cascades/haarcascade_eye.xml")
    camera = cv2.VideoCapture(0)

    while True:
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5, 0, (40, 40))
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(frame, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 255, 0), 2)
        cv2.imshow("camera", frame)
        if cv2.waitKey(1000/12) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect()