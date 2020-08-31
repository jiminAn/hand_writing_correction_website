
import cv2
import numpy as np
import matplotlib.image as mp_image
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from PIL import Image


img = cv2.imread("./test_data/example.PNG")
#model = load_model('emnist_trained.h5')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

ret, img_th = cv2.threshold(img_blur, 100, 230, cv2.THRESH_BINARY_INV)

contours, hierachy= cv2.findContours(img_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

rects = [cv2.boundingRect(each) for each in contours]

tmp = [w*h for (x,y,w,h) in rects]
print(tmp)
#rects = [(x,y,w,h) for (x,y,w,h) in rects if ((w*h>15000)and(w*h<500000))]
#rects

for rect in rects:
    cv2.rectangle(img, (rect[0], rect[1]), 
                  (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 5) 
    print(rect[0], rect[1], rect[2], rect[3])
    area = (rect[0], rect[1],rect[2], rect[3])
    cropped = img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
    cv2.imshow("crop",cropped);
