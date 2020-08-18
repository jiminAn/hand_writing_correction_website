from keras.models import Sequential
from keras.layers import Dropout, Activation, Dense
from keras.layers import Flatten, Convolution2D, MaxPooling2D
from keras.models import load_model
import cv2
from keras.callbacks import ModelCheckpoint,EarlyStopping
import os
import datetime

allow_pickle = True
X_train, X_test, Y_train, Y_test = np.load('./img_data.npy', allow_pickle=True)#read_img에서 만든 데이터 셋을 불러옴

#모델 훈련은 Sequential/Convolution2D/Maxpooling2D/Flatten/Dense 과정 찾아보면서 공부

model = Sequential()
model = Sequential()
#X_train.shape[1:] = (28,28,3) -> read_image.py에서 grayscale변경시 (28,28,1)
#만약에 ValueError: Negative dimension size caused by subtracting오류 뜰 시 뒤에 data_format="channels_last"/channels_first추가
#혹은 terminal 열어서 keras.json에서 image_data_format : channels_first로 직접변경해줘야함
model.add(Convolution2D(16, 3, 3, padding='same', activation='relu',input_shape=X_train.shape[1:]))#케라스버전에따라border_mode/padding
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
  
model.add(Convolution2D(64, 3, 3,  activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
 
model.add(Convolution2D(64, 3, 3))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
  
model.add(Flatten())
model.add(Dense(256, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes,activation = 'softmax'))
  
model.compile(loss='binary_crossentropy',optimizer='Adam',metrics=['accuracy'])
model.fit(X_train, Y_train, batch_size=32, nb_epoch=100)
 
#모델을 저장할 경로와 파일명을 지정
model.save('Gersang.h5')

X_train = np.append(X_train,X_test, axis=0)
Y_train = np.append(Y_train,Y_test, axis=0)
 

Datetime = datetime.datetime.now().strftime('%m%d_%H%M')
modelpath="Gersang.h5"
 
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='loss', verbose=1, save_best_only=True)
early_stopping_callback = EarlyStopping(monitor='loss', patience=100)
 
# Learning and save models
model.fit(X_train, Y_train, validation_split=0.1, epochs=3500, batch_size=10, verbose=0, callbacks=[early_stopping_callback,checkpointer])


