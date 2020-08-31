## Ex 10-6. EMNIST 손글씨 인식 프로그램.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import tensorflow as tf
from PIL import Image
import matplotlib.image as mp_image
import cv2


def make_square(im, min_size=256, fill_color=(255, 255, 255, 255)):
    size = 400
    rows, cols, channels = im.shape
    new_im = Image.new('RGB', (size, size), "white")
    new_im = np.array(new_im)
    roi = new_im[0:rows, 0:cols]
    #cv2.imshow('mask_inv',roi)
    img2gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    #cv2.imshow('mask_inv',mask_inv)

    img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
    #cv2.imshow('mask_inv',img1_bg)
    img2_fg = cv2.bitwise_and(im, im, mask = mask)
    #cv2.imshow('mask_inv',img2_fg)
 
    dst = cv2.add(img1_bg, img2_fg)
    #cv2.imshow('mask_inv',dst)
    x = (size-rows)/2
    y = (size-cols)/2
    new_im[0:rows, 0:cols] = img2_fg
    #cv2.imshow("img", new_im)
    cv2.imwrite('alpha.PNG', new_im)
    return new_im

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.image = QImage(QSize(400, 400), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.brush_size = 30
        self.brush_color = Qt.black
        self.last_point = QPoint()
        self.loaded_model = None
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('File')

        load_model_action = QAction('Load model', self)
        load_model_action.setShortcut('Ctrl+L')
        load_model_action.triggered.connect(self.load_model)

        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save)

        clear_action = QAction('Clear', self)
        clear_action.setShortcut('Ctrl+C')
        clear_action.triggered.connect(self.clear)

        filemenu.addAction(load_model_action)
        filemenu.addAction(save_action)
        filemenu.addAction(clear_action)

        self.statusbar = self.statusBar()

        self.setWindowTitle('EMNIST Classifier')
        self.setGeometry(300, 300, 400, 400)
        self.show()

    def paintEvent(self, e):
        canvas = QPainter(self)
        canvas.drawImage(self.rect(), self.image, self.image.rect())

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = e.pos()

    def mouseMoveEvent(self, e):
        if (e.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
            painter.drawLine(self.last_point, e.pos())
            self.last_point = e.pos()
            self.update()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drawing = False

            arr = np.zeros((28, 28))
            for i in range(28):
                for j in range(28):
                    arr[j, i] = 1 - self.image.scaled(28, 28).pixelColor(i, j).getRgb()[0] / 255.0
            arr = arr.reshape(28, 28)

            if self.loaded_model:
                arr = arr.flatten().reshape(-1, 28*28)
                pred = self.loaded_model.predict(arr)[0]
                pred_num = int(np.argmax(pred))
                alpha = chr(pred_num+64)
                self.statusbar.showMessage('알파 ' + alpha + '입니다.')

    def load_model(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Load Model', './model1.h5')


        if fname:
            self.loaded_model = tf.keras.models.load_model(fname)
            self.statusbar.showMessage('Model loaded.')

    def save(self):
        self.image.save("test.PNG")
        img = cv2.imread("test.PNG")
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
        ret, img_th = cv2.threshold(img_blur, 100, 230, cv2.THRESH_BINARY_INV)
        contours, hierachy= cv2.findContours(img_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        rects = [cv2.boundingRect(each) for each in contours]
        tmp = [w*h for (x,y,w,h) in rects]

        predict = []
        for rect in rects:
            cropped = img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
            make_square(cropped);
            img = cv2.imread("alpha.PNG")
            if self.loaded_model:
                img = cv2.resize(img, dsize = (28, 28), interpolation = cv2.INTER_AREA)
                cv2.imshow("img", img)
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                x = img_gray.reshape(1, 28*28)
                y = self.loaded_model.predict(x)[0]
                pred_num = int(np.argmax(y))
                print(chr(pred_num+64))


    def clear(self):
        self.image.fill(Qt.white)
        self.update()
        self.statusbar.clearMessage()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.load_model()
    sys.exit(app.exec_())