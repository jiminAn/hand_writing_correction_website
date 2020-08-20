# LOG : handwritten english alphabet recognition web project 

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

