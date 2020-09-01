# Web Programming LOG

#### **Project Name**

Handwriting Correction Website

#### **Developer**

- [limjustin](https://github.com/limjustin)

<br/>

## 2020-08-20 (Thu)

**Server-Side**

1. **Server 만들기**
   - http 사용하여 기본적인 Node.js Web Server 구현

**Client-Side**

1. **사용자 그림판**

   - Client 화면 위에 Canvas 보여주기

   - Canvas 위에 사용자가 직접 그림 그릴 수 있도록 하기

2. **이미지 저장 기능**
   - 사용자가 그린 그림을 png 파일로 변환하여 저장할 수 있도록 하기

<br/>

## 2020-08-21 (Fri)

**Client-Side**

1. **Python 코드 구동에 관한 연구**
   - 큰 구조 정도만 생각

<br/>

## 2020-08-22 (Sat)

**Server Side**

1. **html 파일과 외부 js 파일 연결**

   - jQuery

   - script 태그 개념

2. **Express js Server 기본 Setting 적용**

3. **Python 코드 관련 고민**

   - Python 코드는 Server에서 구동되어야 한다는 것을 알아냄

   - Python 코드 구현 연구 중 (상당히 어려움)

<br/>

## 2020-08-23 (Sun)

**Server-Side**

1. **Python 코드 구동에 관한 기초적인 연구**

   - 코드의 기본적인 구성 요소 다시 확인해보는 중 (Input, Output)

     - 문제점 : **require( ) 메소드는 Client에서 사용할 수 없음** (2번으로 확장)

     - 해결 : **Ajax GET 방식 사용하여 Client에서 Server 호출하여 해결**

2. **Client에서 Server를 호출하는 방법 연구**

   - Ajax 개념 공부하는 중 (GET and POST)

   - Ajax를 이용하여 GET/POST 통신 진행하면 해결 (우선적으로 GET 방식 사용)

     - 문제점 : **Server에서 Python 코드를 호출할 수 있는 방법을 모름** (3번으로 확장)

     - 해결 : **child_process 사용하여 Python과 Node.js 사이 Communication 가능**

3. **Python 코드 호출 방식 연구**

   - js file에서 외부 Python 코드를 실행할 수 있는 방법 찾는 중
     - 해결 : **child_process라는 Node.js 모듈 사용하여 Python 코드 구동 가능**
     - 미확인 : **복잡한 코드도 실행될 것인가?**

**Client-Side**

1. **Client에서 Server를 호출하는 방법**
   - Ajax를 이용하여 GET/POST 통신 진행하면 해결

**Completed Function**

- 사용자 그림판 기능
- 이미지 파일 저장 기능
- Express.js 서버 구현
- 외부 Python 파일 실행

<br/>

## 2020-08-24 (Mon)

**Server and Client**

1. Structure 생각

**Plus Alpha**

1. Class Diagram 공부
2. Sequence Diagram 공부

<br/>

## 2020-08-25 (Tue)

**Server-Side**

1. Server 디렉토리 만든 후에 그 디렉토리에 있는 파일 Run 하는 방법

**Server and Client**

1. 큰 구조 생각

<br/>

## 2020-08-26 (Wed)

**Server-Side**

1. 바로바로 데이터가 들어오면 반응해줄 수 있는 웹을 만들어야 하나

**Client-Side**

1. 글자를 분할하여 저장하도록 하면 Client에게 어떤 식으로 명시해주어야 하나
2. 글자 수 제한이 분명히 생길텐데 이런 점을 어떤 식으로 명시해주어야 하나

<br/>

## 2020-08-27 (Thu)

**Client-Side**

1. CSS 부분 디자인

<br/>

## 2020-08-28 (Fri)

**Client-Side**

1. CSS 부분 디자인

**Python**

1. 인공지능 학습 코드 공부

<br/>

## 2020-08-29 (Sat)

**Client and Server**

1. Download 버튼 만들어서 이미지 확인 (경로 설정의 문제는?)
2. 저장 경로를 내가 지정할 수는 없을까?
   - 사용자 Download 폴더에만 가능한 것인가...
   - 그렇다면 중복되는 파일 명은 어떻게 해결할 것인가?
     - 난수 생성을 통하여 숫자 고유번호 안겹치도록 파일 이름 생성하기
     - 이것을 파이썬 코드로 어떻게 전달할 것인가? (html<->js<->py 3대 대통합 필요)

**Completed Function**

1. 사용자 그림판 기능
2. 이미지 파일 저장 기능
3. Express.js 서버 구현
4. 외부 Python 파일 실행
5. 그림판 CSS 완성
6. 파일 안겹치도록 이미지 생성 가능

<br/>

## 2020-08-30 (Sun)

**Client and Server**

1. **Ajax와 Python 연결할 때 헷갈리는 개념 정리 완료**
   - Datatype : text와 json
   - py.stdin.write(JSON.stringify(req.query.data))
2. **Font 종류 및 설정**
   - js 파일에서 돌아갈 수 있도록 함수 구현 (isChecked 판정 역할)
3. **생각지도 못했던 점**
   - Canvas를 하나만 사용하는 것은 되는데, 두개를 사용하게 되면 사용자 화면에 있는 마우스 좌표를 인식하는 것이라 안됨
   - 한 html 페이지 안에서 두 개의 캔버스를 사용한다는 것은 안됨
   - 따라서 html 페이지를 나눠야 함 (처음에는 나눈다고 생각 안하고 있었음)
   - 그러면 html끼리 데이터를 넘기는 작업이 필요
     1. **Ajax 호출 방식 사용**
        - 문제점 1: 너무 코드가 복잡해지고, 호출 관계도 복잡해짐.
        - 문제점 2: 무엇보다도, ajax를 호출하는 html과 값을 받아낼 html이 서로 다르기 때문에 이 부분 해결할 수 없음.
     2. **url 상에 담아서 옮기기**
        - 문제점 1: 새로운 도메인이 생성되어 제대로 화면이 넘어갈 수 없음.
     3. **Database 사용 - MongoDB**
        - 문제점 1: MongoDB를 require( ) 메소드를 사용하여 불러와야 하는데, require( ) 메소드는 Client에서 사용 못 함
        - 문제점 2: 따라서 Client에서 데이터를 저장하고 싶지만, 마음대로 잘 안됨.
     4. **localStorage와 sessionStorage**
        - 해결 : Client에서 데이터를 저장할 수 있게 하는 변수

**Client**

1. **Font 종류 및 설정**
   - Checkbox, Table 개념 학습

<br/>

## 2020-08-31 (Mon)

**Client and Server**

1. sessionStorage 방식 사용하여 데이터 넘기기 성공
2. 모든 기능 연결

**Etc**

1. 예외사항 논의

<br/>

## 2020-09-01 (Tue)

**Client and Server**

1. **한 줄 이상 문자열 결과 나오는 것 연동**
   - split( ) 함수 사용하여 각 배열로 저장

**Client-Side**

1. **기본 UI 완성**
   - css-style 태그 사용하여 정렬
   - css file 사용
2. **Canvas 기능 고민**
   - result.html 창에서 Canvas가 이상한 좌표에 그려지는 것을 파악
   - 교훈 : 화면에 그려지는 것은 너무나 어렵다. 사용자마다 친화적이게 디자인 할 수는 없을까?
3. **한 줄 이상 문자열 결과 나오는 것 연동**
   - html에 보여주기까지 완성

**Completed Function**

- All Function is clear

**Remain Things**

- Download Loading Function
- Exceptions Check

<br/>