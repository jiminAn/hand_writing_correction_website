import sys, os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm

font_path = "C:/Users/forea/PycharmProjects/untitled/font/"
fonts = os.listdir("C:/Users/forea/PycharmProjects/untitled/font/")

co = "0 1 2 3 4 5 6 7 8 9 A B C D E F"
upper_start = "0041" # 대문자 시작
upper_end = "005A" # 대문자 끝

lower_start = "0061" # 소문자 시작
lower_end = "007A" # 소문자 끝


co = co.split(" ")

English_Syllables = [a+b+c+d
                    for a in co
                    for b in co
                    for c in co
                    for d in co] # 사중 포문

English_Syllables = np.array(English_Syllables)
us = np.where(upper_start == English_Syllables)[0][0] # 대문자 유니코드 시작
ue = np.where(upper_end == English_Syllables)[0][0] # 대문자 유니코드 끝

ls = np.where(lower_start == English_Syllables)[0][0] # 소문자 유니코드 시작
le = np.where(lower_end == English_Syllables)[0][0] # 소문자 유니코드 끝

Upper_English_Syllables = English_Syllables[us : ue + 1] # 구간 저장
Lower_English_Syllables = English_Syllables[ls : le + 1]

for uni in tqdm(Upper_English_Syllables):
    unicodeChars = chr(int(uni, 16))
    path = "./English_Syllables/" + unicodeChars # 경로
    os.makedirs(path, exist_ok=True) # 파일 경로 생성

    for ttf in fonts:
        font = ImageFont.truetype(font=font_path + ttf, size=100) # 폰트를 이미지화
        x, y = font.getsize(unicodeChars) # 폰트의 사이즈를 가져옴
        theImage = Image.new('RGB', (x, y), color='white') # (색상, 이미지 크기, 이미지 바탕)
        theDrawPad = ImageDraw.Draw(theImage)  #이미지를 그림
        theDrawPad.text((0,0), unicodeChars[0], font=font, fill='black') # (그림을 저장할 좌표 위치, 타입, 폰트, 글씨 색)
        msg = path + "/" + ttf[:-4] + "_" + unicodeChars #경로 ( 파일 이름에 .ttf를 없애기 위해 -4로 슬라이싱)
        theImage.save('{}.jpg'.format(msg)) # 저장

for uni in tqdm(Lower_English_Syllables):
    unicodeChars = chr(int(uni, 16))
    path = "./English_Syllables/" + unicodeChars # 경로
    os.makedirs(path, exist_ok=True) # 파일 경로 생성

    for ttf in fonts:
        font = ImageFont.truetype(font=font_path + ttf, size=100) # 폰트를 이미지화
        x, y = font.getsize(unicodeChars) # 폰트의 사이즈를 가져옴
        theImage = Image.new('RGB', (x, y), color='white') # (색상, 이미지 크기, 이미지 바탕)
        theDrawPad = ImageDraw.Draw(theImage)  #이미지를 그림
        theDrawPad.text((0,0), unicodeChars[0], font=font, fill='black') # (그림을 저장할 좌표 위치, 타입, 폰트, 글씨 색)
        msg = path + "/" + ttf[:-4] + "_" + unicodeChars + "_" + "lower" #경로 ( 파일 이름에 .ttf를 없애기 위해 -4로 슬라이싱)
        theImage.save('{}.jpg'.format(msg)) # 저장
