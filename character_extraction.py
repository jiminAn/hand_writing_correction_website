import cv2
import numpy as np
import matplotlib.pyplot as plt

# Ver 1.0 강대훈 (초안 및 주석 작성)
# 필터를 추가해서 실행할 필요가 있음

img = cv2.imread("C:/Users/forea/PycharmProjects/untitled/abs.jpg") # 글씨를 추출할 이미지
idx= 0 # 번호
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # RGB -> Gray
thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] # Gray로 변환해야 코드 사용 가능
# cv2.threshold(img, threshold_value, value, flag)
# img:grayScale이고 threshold_value는 픽셀 문턱값이고 문턱값 이상이면 value로 바꿈

#THRESH_BINARY_INV  : threshold보다 크면 0이고 아니면 value로 바꾸어 줌
#THRESH_BINARY: threshold보다 크면 value이고 아니면 0으로 바꾸어 줌
#THRESH_OTSU : 이미지 히스토그램을 분석한 후 중간 값을 threshold_value에 저장
# https://webnautes.tistory.com/1254 참고

# Contours란 동일한 색 또는 동일한 강도를 가지고 있는 영역의 경계선을 연결한 선
# OpenCV에서 contours를 찾고, 그리기 위해서 아래 2개의 함수를 사용합니다.
# cv2.RETR_TREE : 모든 contours line을 찾음
# cv2.CHAIN_APPROX_SIMPLE:  contours line을 그릴 수 있는 4개의 point 만 저장

cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #
cnts = cnts[0] if len(cnts) == 2 else cnts[1] # 이 코드는 잘 모르겠음

rects = [cv2.boundingRect(each) for each in cnts]

for (x,y,w,h) in rects:
    # Draw the rectangles
    #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5) # 인식한 것에 사각형 표시
    cropped = img[y - int(h / 4):y + h + int(h / 4), x - int(w / 4):x + w + int(w / 4)] # 잘라내서
    cv2.imwrite(str(idx) + ".jpg", cropped) # 이름 붙여줘서 저장
    idx+=1
