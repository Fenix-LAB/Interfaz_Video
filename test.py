import cv2
import time

cap = cv2.VideoCapture(0) # VideoCapture("la camara")

# if not cap.isOpened():
#     print("No se pudo abrir la cámara")
#     exit()

while True:
    ret, img = cap.read()
    # if not ret:
    #     print("No se pudo recibir el marco")
    #     break
    if ret:
        # print(img)
        #imgR = cv2.resize(img, (640,640))
        cv2.imshow('Picture', img)

    # Es necesario tener un codigo para salir del ciclo While
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()