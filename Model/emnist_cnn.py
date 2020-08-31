# 모델 학습 과정 표시하기

#
# filename : emnist_cnn.py
# history
# =============================
# 20200826 Ver 1.0 초안 작성 (안지민)
# =============================
# Ver 1.0

# Visualization Dependencies
from IPython.display import Image, SVG
import seaborn as sns

# Filepaths, Numpy, Tensorflow
import os
import numpy as np
import tensorflow as tf

# Keras
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras import backend as K
from tensorflow.keras.datasets import mnist
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

#ignore warning messages
import warnings
warnings.filterwarnings('ignore')

sns.set()


# pip install emnist
# Import Dataset(s)
from emnist import list_datasets
list_datasets()

from emnist import extract_training_samples
images_train, labels_train = extract_training_samples('letters')
from emnist import extract_test_samples
images_test, labels_test = extract_test_samples('letters')

# Flatten Data
dims = images_train.shape[1] * images_train.shape[2]
X_train = images_train.reshape(images_train.shape[0], dims)
X_test = images_test.reshape(images_test.shape[0], dims)


# Rescale to 0 -> 1 by dividing by max pixel value (255)
X_train = X_train.astype('float32')/255
X_test = X_test.astype('float32')/255


# One-Hot Encoding

from keras.utils import np_utils # used to convert array of labeled data to one-hot vector
# should be 26 but out of index?
# Effects accuracy as have a class where their will be no results
num_classes = 27
y_train = np_utils.to_categorical(labels_train, num_classes)
y_test = np_utils.to_categorical(labels_test, num_classes)


# Empty Sequential model
from tensorflow.keras.models import Sequential
model = Sequential()

#Layers

# 1 - number of elements (pixels) in each image
# Dense layer - when every node from previous layer is connected to each node in current layer
model.add(Dense(500, activation='relu'))

# Second Hidden Layer
model.add(Dense(500, activation='relu'))

# Output Layer - number of nodes corresponds to number of y labels
model.add(Dense(num_classes, activation='softmax'))

# Compile Model
model.compile(loss='categorical_crossentropy', optimizer='rmsprop' , metrics=['accuracy'])


# Train Model
model.fit(X_train, y_train, batch_size=128, epochs=10, shuffle=True, verbose=2)

model.summary()

# Save Model
model.save("emnist_trained.h5")
