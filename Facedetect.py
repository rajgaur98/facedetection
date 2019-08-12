import cv2
from tkinter import *


def fd():
    face_cascade = cv2.CascadeClassifier(
        "C:\\Users\\Gaur\\PycharmProjects\\miniproject\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml")

    video = cv2.VideoCapture(0)
    a = 1
    while True:



        check, frame = video.read()

        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

        for x,y,w,h in faces:
            frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            if a is 1:
                print('human face detected')
                cv2.imwrite("f1.jpg", frame)
            a = a+1

        cv2.imshow("win", frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            break
        elif key == ord('m'):
            cv2.imwrite("extra.jpg", frame)

    video.release()

    cv2.destroyAllWindows()


root = Tk()

root.geometry("600x300")

label_1 = Label(root, text="\n\nAutomatic Face Detection\n\n")

label_1.pack()

label_3 = Label(root, text="Click 'Start' to start automatic face detection\n\nNote: As soon as human face appears in front of camera image would be clicked and saved\n\nPress 'm' for saving extra image\n\nPress 'q' to end detection\n\n" )

label_3.pack()

button_1 = Button(root, text = "Start", command = fd)

button_1.pack()

root.mainloop()