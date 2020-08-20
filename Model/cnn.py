from keras.models import Sequential
from keras.layers import Dropout, Activation, Dense
from keras.layers import Flatten, Convolution2D, MaxPooling2D
from keras.models import load_model
import numpy as np
import cv2
from keras.callbacks import ModelCheckpoint, EarlyStopping
import os
import datetime

allow_pickle = True
X_train, X_test, Y_train, Y_test = np.load('./img_data.npy', allow_pickle=True)  # read_img에서 만든 데이터 셋을 불러옴
#
# filename : cnn.py
# history
# =============================
# 20200820 v.1.0 초안 작성 안지민
# 20190903 v.1.1 padding, input_shape 값 수정 강대훈
# =============================
# Ver 1.1 
model = Sequential()
print(X_train.shape)
model.add(Convolution2D(16, 3, 3, padding='same', activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
model.add(Dropout(0.25))

model.add(Convolution2D(64, 3, 3, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
model.add(Dropout(0.25))

model.add(Convolution2D(64, 3, 3, padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])
model.fit(X_train, Y_train, batch_size=32, epochs=50)

# 모델을 저장할 경로와 파일명을 지정
model.save('hand_writing.h5')

X_train = np.append(X_train, X_test, axis=0)
Y_train = np.append(Y_train, Y_test, axis=0)

Datetime = datetime.datetime.now().strftime('%m%d_%H%M')
modelpath = "hand_writing.h5"

checkpointer = ModelCheckpoint(filepath=modelpath, monitor='loss', verbose=1, save_best_only=True)
early_stopping_callback = EarlyStopping(monitor='loss', patience=100)

# Learning and save models
model.fit(X_train, Y_train, validation_split=0.1, epochs=3500, batch_size=10, verbose=0,
          callbacks=[early_stopping_callback, checkpointer])
