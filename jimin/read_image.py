import os
import cv2
import numpy as np

from sklearn.model_selection import train_test_split

groups_folder_path = './cnn_sample/Fnt/' #alphabet이 저장되어 있는 경로 설
categories = [] # 이미지 카테고리

#categories에 file경로 이름 붙이는 반복문
for i in range(1,63):
    if i < 10:
        categories.append("Sample00" + str(i))
    else:
        categories.append("Sample0" + str(i))

num_classes = len(categories)

# 사이지 28x28로 크기 줄이기
image_w = 28
image_h = 28

X = []
Y = []

#catagiories(순서가 있는 자료형인 리스트)을 입력으로 받아 인덱스 값을 포함하는 enumerate객체를 반환
for idex, categorie in enumerate(categories):
    label = [0 for i in range(num_classes)]
    label[idex] = 1
    image_dir = groups_folder_path + categorie + '/'

    for top, dir, f in os.walk(image_dir):
        for filename in f:
            print(image_dir + filename)
            img = cv2.imread(image_dir + filename)
            img = cv2.resize(img, None, fx=image_w / img.shape[0], fy=image_h / img.shape[1])
            X.append(img / 256)
            Y.append(label)

X = np.array(X)
Y = np.array(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
xy = (X_train, X_test, Y_train, Y_test)

np.save("./img_data.npy", xy)


