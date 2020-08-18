#생성된 모델로 테스트하는 코드
import os, re, glob
import cv2
import numpy as np
import shutil
from numpy import argmax
from keras.models import load_model
 
#분류할 카테고리 지정: 단, read_img.py에서와 카테고리 분류 이름 동일해야함 
categories = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
              "A", "C", "D", "E", "F", "H", "J","K", "L", "M",
              "N", "R", "S", "T", "X", "Y", "Z"]
 
def Dataization(img_path):
    image_w = 28
    image_h = 28
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0])
    return (img/256)
 
src = []
name = []
test = []
image_dir = "/Users/mac/PycharmProjects/handwritten_cnn_project/test_data/" #테스트할 이미지 폴더 경로: 각자 경로 맞게 설정할 것
for file in os.listdir(image_dir):
    if (file.find('.png') is not -1):      
        src.append(image_dir + file)
        name.append(file)
        test.append(Dataization(image_dir + file))
 
 
test = np.array(test)
model = load_model('Gersang.h5') #사용할 모델 불러오기
predict = model.predict_classes(test)
 
for i in range(len(test)): # 알파벳 예측 결과 출력
    print(name[i] + " : , Predict : "+ str(categories[predict[i]]))

