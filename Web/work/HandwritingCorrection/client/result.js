// To do List in result.js //
// 0. main.html 스크롤 없애야 할 것 같은데
// 1. 받은 array를 콤마(,) 단위로 분류하는 작업
// 2. 분류한 Font를 배열에 넣는 작업 (push나 pop 사용?)
// 3. 글씨를 선택할 수 있게 해야함 (예전에 세션 사용해서 해시태그처럼 띄운거 생각해보기)
// 4. 선택한 글씨를 Canvas에 띄우는 것까지

const myCanvas = document.querySelector('#myCanvas');
const ctx = myCanvas.getContext("2d");

// 시작하자마자 보여주는 함수
window.onload = function() {
    // 넘어온 데이터 받아서 저장
    var array = new Array();
    array = sessionStorage.getItem('array');
    console.log(array);

    var result = sessionStorage.getItem('result'); // Python 코드 결과값

    console.log(sessionStorage.getItem('url'));
    const imgConverted = document.querySelector("#imgConverted");
    imgConverted.src = sessionStorage.getItem('url'); // 이미지 보여주는 역할

    // 배열 분리
    var newStr = array.split(",");
    for(var i = 0; i < newStr.length; i++) {
        console.log(newStr[i]);
    }

    document.getElementById("demo").innerHTML = ""; // 태그 초기화 작업

    newStr.forEach(function(element) {
        document.getElementById("demo").innerHTML += "<button id=\"fontButton\" onclick=\"setFont(this.value)\" value=\"" + element + "\"" + ">" + element + "</button><br>";
    });

    $('#showBlack').html(result);
    // const showBlack = document.querySelector("#showBlack");
    // $('#showBlack').css(font-family);
    console.log($('#showBlack').css("font-family"));
    console.log($('#showBlack').css("font-family"));
}

function setFont(e) {
    console.log(e);
    // console.log($(this).attr('value')); // 눌린것의 value를 찾아야하는데
    $('#showBlack').css("font-family", e);

    var font = $('#showBlack').css("font-family");
    console.log("font is " + font);

    if(font == "Arial") { // 문자열은 Double Quote가 하나 더 붙는구나?
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Arial";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "\"Times New Roman\"") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Times New Roman";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "Helvetica") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Helvetica";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "Times") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Times";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "\"Courier New\"") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Courier New";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "Verdana") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Verdana";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "Courier") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Courier";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "\"Arial Narrow\"") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Arial Narrow";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "Candara") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Candara";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "Geneva") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Geneva";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "Calibri") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Calibri";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "Optima") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Optima";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "ArCambriaial") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px ArCambriaial";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "Garamond") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Garamond";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "Perpetua") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Perpetua";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "Monaco") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Monaco";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "Didot") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Didot";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "\"Brush Script MT\"") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Brush Script MT";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "\"Lucida Bright\"") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Lucida Bright";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    else if(font == "Copperplate") {
        ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
        ctx.font = "150px Copperplate";
        ctx.fillStyle = "silver";
        ctx.fillText(sessionStorage.getItem('result'),500, 500);
    }
    console.log("ctx.font is " + ctx.font);

    // console.log(font);

    // ctx.font = "200px Times New Roman";
    // console.log(ctx.font);  
}