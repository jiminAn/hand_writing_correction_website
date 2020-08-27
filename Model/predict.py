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

def get_square(image,square_size):

       (height,width)=image.shape[:2]
       if(height>width):
         differ=height
       else:
         differ=width
       differ+=4
       image = cv2.resize(image, (width, height))

       mask = np.zeros((differ,differ), dtype="uint8")   
       x_pos=int((differ-width)/2)
       y_pos=int((differ-height)/2)
       mask[y_pos:y_pos+height,x_pos:x_pos+width]=image[0:height,0:width]
       mask=cv2.resize(jk,(square_size,square_size),interpolation=cv2.INTER_AREA)

       return mask 


def make_square(im, min_size=256, fill_color=(255, 255, 255, 255)):
    size = 400
    (x, y) = im.shape[:2]
    #size = max(min_size, x, y)
    bbox = (0, 0, int((size - x) / 2), int((size - y) / 2))
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im = np.array(new_im)
    roi = new_im[0:100, 0:100]
    img2gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    img2_fg = cv2.bitwise_and(im, im, mask = mask)

    dst = cv2.add(img1_bg, img2_fg)
    img1[0:100, 0:100] = dst
    cv2.imshow("img", dst)
    return dst

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
        #fpath, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        self.image.save("test.PNG")
        img = cv2.imread("test.PNG")
        #cv2.imshow("img", img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("img", img_gray)
        img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
       # cv2.imshow("img", img_blur)
        ret, img_th = cv2.threshold(img_blur, 100, 230, cv2.THRESH_BINARY_INV)
        contours, hierachy= cv2.findContours(img_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        rects = [cv2.boundingRect(each) for each in contours]
        tmp = [w*h for (x,y,w,h) in rects]

        predict = []
        for rect in rects:
            print(rect)
            #image2 = np.array(image2)
            #cv2.rectangle(img, (rect[0], rect[1]), 
            #      (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 5) 
   
            #print(rect[0], rect[1], rect[2], rect[3])
            cropped = img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
            #cropped = make_square(cropped)
            print(cropped.shape)
            cv2.imwrite('alpha.PNG', cropped)
            arr = cv2.imread('alpha.PNG')
            arr = cv2.resize(arr, (28, 28))
            arr = arr.reshape(-1, 28*28)
            cv2.imshow("img",arr)

            pred = self.loaded_model.predict(arr)[0]
            pred_num = int(np.argmax(pred))
            print(chr(pred_num+64))
            predict.append(chr(pred_num+64))

       # self.statusbar.showMessage('저장된 문자열은 ' , predict ,'입니다.')
  
            
        #if fpath:
            #self.image.scaled(28, 28).save(fpath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()
        self.statusbar.clearMessage()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.load_model()
    sys.exit(app.exec_())