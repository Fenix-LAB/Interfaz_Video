from gui_design import *
from PyQt5.QtGui import  QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal
import cv2
import imutils

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
# Se define le contructor con todos los atributos necesarios y asociacion de metodos
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.star_video()


    def star_video(self):
        self.work = Work()
        self.work.start()
        self.work.img_update.connect(self.update_picture)

    def update_picture(self, Image):
        self.WIDGET_IMG.setPixmap(QPixmap.fromImage(Image))


## Esta es una clase que se corre en un hilo diferente al principal
class Work(QThread):
    img_update = pyqtSignal(QImage)

    def run(self):
        cap = cv2.VideoCapture(0)
        self.run_thread = True
        while self.run_thread:
            ret, img = cap.read()
            # if not ret:
            #     print("No se pudo recibir el marco")
            #     break
            if ret:
                # print(img)
                # imgR = cv2.resize(img, (640,640))
                # cv2.imshow('Picture', img)
                frame_flip = cv2.flip(img, 1)
                frame_r = imutils.resize(frame_flip, width=640, height=480)

                pic_qt = QImage(frame_r.data, frame_r.shape[1], frame_r.shape[0], QImage.Format_BGR888)

                self.img_update.emit(pic_qt)

    def stop(self):
        self.run_thread = False
        self.quit()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyApp()
    window.show()
    app.exec_()