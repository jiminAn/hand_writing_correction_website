# Web Programming LOG

#### **Project Name**

Handwriting Correction Website

#### **Developer**

- [limjustin](https://github.com/limjustin)

<br></br>

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

<br></br>

## 2020-08-21 (Fri)

**Client-Side**

1. **Python 코드 구동에 관한 연구**
   - 큰 구조 정도만 생각

<br></br>

## 2020-08-22 (Sat)

**Server Side**

1. **html 파일과 외부 js 파일 연결**

   - jQuery

   - script 태그 개념

2. **Express js Server 기본 Setting 적용**

3. **Python 코드 관련 고민**

   - Python 코드는 Server에서 구동되어야 한다는 것을 알아냄

   - Python 코드 구현 연구 중 (상당히 어려움)

<br></br>

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