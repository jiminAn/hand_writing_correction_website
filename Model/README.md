# LOG : AI model

## 2020.8.14
1. 데이터 분석  : 숫자+알파벳 데이터
56019_107433_bundle_archive  
- English -> Fnt -> Sample001~062 : 폰트별로 섹션 정리되어 있음
- English2  -> Img -> BadImag : 인식하기 어려운 bmp/msk file로 섹션 별 정리
- English2  -> Img -> GoodImag : 인식하기 좋은 bmp/msk file로 섹션 별 정리

2. 자신만의 이미지 데이터로 CNN 적용해보기
- https://twinw.tistory.com/252
: 이미지 파일 학습 데이터로 변경하기 (완) read_image.py (2020_08_16)

## 2020.8.18

1. 생성된 데이터셋으로 훈련하기  
: cnn.py
2. 생성된 모델로 테스트 하기  
: model_test.py

## 2020.8.20
1. gray scale로 변환 성공
: read_image
2. 패딩 값 same으로 변환
:cnn.py
3. epocs당 평균 acc 60 -> 데이터 변경 및 CNN 알고리즘 개선 필요
4. model.add(Dropout(0.1)) 0.25에서 0.1로 바꿀시 정확도 평균 0.89
5. model.add(Dropout(0.05)) 0.25에서 0.05로 바꿀시 정확도 평균 0.92

## 2020.08.22
1. 전체 데이터 세트 개수: 약 63,000개
2. train set/ test set 분류 관련 참고  
- link <https://teddylee777.github.io/scikit-learn/train-test-split>  
- read_img.py v.0.1.0 에서는 train : set = 7.5 : 2.5(train_test_split : default)
3. 과적합(overfitting) 확인하기  
- link <https://ganghee-lee.tistory.com/38>
- 주피터노트북을 통해 그래프 그려 확인-> 적절한 epoch값 찾기

## 2020.08.23
1. 과적합 해결 방법
- 훈련 데이터 개수 늘리기 : 63,000->126,000 두 배로 늘렸으나 해결 안됨 + 훈련 시간 너무 오래 걸림  
- 모델 학습 과정 살펴보기    
: 참고 <https://tykimos.github.io/2017/07/09/Early_Stopping/>  
2. 과적합 진단을 위한 모델 학습과정 그래프로 그리기    
: check_overfitting_graph.py  
: read_img 부분에 주석 추가와 학습과정을 기록하기 위해 hist변수 추가  

## 2020.08.25
1. 학습 데이터 바꿔보기   
- 참고 <https://sdc-james.gitbook.io/onebook/4.-and/5.4.-tensorflow/5.4.2.-cnn-convolutional-neural-network>  

## 2020.08.26
1. MNIST로 손글씨 숫자 데이터 학습시키키 : mnist_cnn.py  
- 참고 <https://codetorial.net/tensorflow/mnist_classification.html>
2. EMNIST로 손글씨 알파벳 데이터 학습시키기  : emnist_cnn.py  
- 참고 <https://github.com/ArenD100/Final/blob/master/EMNIST.ipynb>
3. 파이썬 안에서 모델을 불러 그림판으로 input된 데이터에 대해 예측하는 코드 : mnist_my_app.py, emnist_my_app.py  
- 참고 <https://codetorial.net/pyqt5/examples/mnist_classifier.html>

## 2020.08.29 
1. 학습 모델 성능 높이기  
: 에포크 10->100으로 증가하여 emnist_trained.h5 모델 갱신  
2. 특정 알파벳 예측도 높이기  
- 대문자 C/F I/Z N/V R/K U/Y (오른쪽 알파벳을 입력시 왼쪽 알파벳으로 인식함)
- 소문자 b q r(계속 예측값이 다르게 나옴)
