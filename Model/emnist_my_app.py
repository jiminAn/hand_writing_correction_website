# 학습된 모델을 로드하여 <pyQt를 이용해 그린 그림판에 INPUT: 손글씨를 넣어> 모델 정확도 확인

# filename : emnist_my_app.py
# history
# =============================
# 20200826 v.1.0 초안 작성 (안지민)
# =============================
# Ver 1.0

import sys
# for drawing application in python library
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import tensorflow as tf

# drawing application 
class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.image = QImage(QSize(400, 400), QImage.Format_RGB32) #size
        self.image.fill(Qt.white) # background color
        self.drawing = False
        self.brush_size = 30
        self.brush_color = Qt.black
        self.last_point = QPoint()
        self.loaded_model = None
        self.initUI()

    def initUI(self):
        #init MENU BAR
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('File')

        # load AI_model
        load_model_action = QAction('Load model', self)
        load_model_action.setShortcut('Ctrl+L')
        load_model_action.triggered.connect(self.load_model)

        # Save Image  
        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save)

        # Clear Image
        clear_action = QAction('Clear', self)
        clear_action.setShortcut('Ctrl+C')
        clear_action.triggered.connect(self.clear)

        # showing status in file menu
        filemenu.addAction(load_model_action)
        filemenu.addAction(save_action)
        filemenu.addAction(clear_action)

        self.statusbar = self.statusBar()

        # set Title, Size
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

            # rescale the image in Canvas 
            arr = np.zeros((28, 28))
            for i in range(28):
                for j in range(28):
                    arr[j, i] = 1 - self.image.scaled(28, 28).pixelColor(i, j).getRgb()[0] / 255.0
            arr = arr.reshape(28, 28)

            # resize the image for learning in AI_model
            if self.loaded_model:
                arr = arr.flatten().reshape(-1, 28*28) # flatten data
                pred = self.loaded_model.predict(arr)[0] # predict image
                # Change result : int(label) -> character(alphabet)
                pred_num = int(np.argmax(pred)) 
                alpha = chr(pred_num+64) # ASCII 'A' = 65
                self.statusbar.showMessage('알파벳 ' + alpha + '입니다.')

    # load the model using <QFileDialog class>
    def load_model(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Load Model', './emnist_trained.h5')


        if fname:
            self.loaded_model = tf.keras.models.load_model(fname)
            self.statusbar.showMessage('Model loaded.')

    # save the image in Canvas(png/jpg)
    def save(self):
        fpath, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        # scale the image 28x28(same as train_set in AI_model)
        if fpath:
            self.image.scaled(28, 28).save(fpath)

    # clear the image in Canvas
    def clear(self):
        self.image.fill(Qt.white)
        self.update()
        self.statusbar.clearMessage()



if __name__ == '__main__':
    app = QApplication(sys.argv) # create QApplication Class
    ex = MyApp() # create MyApp class
    ex.load_model() # load model <emnist_trained.h5>
    sys.exit(app.exec_()) # exit app
