// To do List in result.js //
// 0. main.html 스크롤 없애야 할 것 같은데
// 1. 받은 array를 콤마(,) 단위로 분류하는 작업
// 2. 분류한 Font를 배열에 넣는 작업 (push나 pop 사용?)
// 3. 글씨를 선택할 수 있게 해야함 (예전에 세션 사용해서 해시태그처럼 띄운거 생각해보기)
// 4. 선택한 글씨를 Canvas에 띄우는 것까지

const clearButton = document.querySelector('.clear');
const stroke_weight = document.querySelector('.stroke-weight');
const color_picker = document.querySelector('.color-picker');

const myCanvas = document.querySelector('#myCanvas');
const canvas = document.querySelector('canvas');
const ctx = canvas.getContext("2d");

let isDrawing = false;
var result;

canvas.addEventListener('mousedown', start);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stop); 

clearButton.addEventListener('click', clearCanvas);

// 시작하자마자 보여주는 함수
window.onload = function() {
    // 넘어온 데이터 받아서 저장
    var array = new Array();
    array = sessionStorage.getItem('array');
    console.log(array);

    result = sessionStorage.getItem('result').split("\n"); // Python 코드 결과값

    
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
        document.getElementById("demo").innerHTML += "<button type=\"button\" class=\"btn btn-danger\" id=\"fontButton\" onclick=\"setFont(this.value)\" value=\"" + element + "\"" + " style=\"margin: 2px 2px 2px 2px; font-family:" + element + "\"" + ">" + element + "</button>";
    });

    $('#showBlack1').html(result[0]);
    $('#showBlack2').html(result[1]);
    // const showBlack = document.querySelector("#showBlack");
    // $('#showBlack').css(font-family);
    console.log($('#showBlack').css("font-family"));
    console.log($('#showBlack').css("font-family"));
}


function start(e) {
    console.log("start function");
    
    isDrawing = true;
    draw(e); // Clicked dot
}

function draw({clientX: x, clientY: y}) {
    console.log("draw function");
    
    if(!isDrawing)
        return;
    
    ctx.lineWidth = stroke_weight.value;
    ctx.lineCap = "round";
    ctx.strokeStyle = color_picker.value;

    ctx.lineTo(x-790, y-130); // 실제 화면상의 마우스 좌표와 캔버스가 나타나는 좌표와 다르면 갭이 생김
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x-790, y-130);
}

function stop() {
    console.log("stop function");
    isDrawing = false;
    ctx.beginPath(); // Create new path not following previous path
}

function clearCanvas() {
    console.log("before clear");
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    pixel();
    console.log("after clear");
}

window.addEventListener('resize', resizeCanvas);
function resizeCanvas() {
    console.log("resize function");
    canvas.width = 680;
    canvas.height = 340;
}
resizeCanvas();

function setFont(e) {
    console.log(e);
    // console.log($(this).attr('value')); // 눌린것의 value를 찾아야하는데
    $('#showBlack').css("font-family", e);

    var font = $('#showBlack').css("font-family");
    console.log("font is " + font);

    ctx.clearRect(0, 0, myCanvas.width, myCanvas.height);
    if(font == "Arial") { // 문자열은 Double Quote가 하나 더 붙는구나?
        ctx.font = "70px Arial";
        ctx.fillStyle = "silver";
    }
    else if(font == "\"Times New Roman\"") {
        ctx.font = "70px Times New Roman";
        ctx.fillStyle = "silver";
    }
    else if(font == "Helvetica") {
        ctx.font = "70px Helvetica";
        ctx.fillStyle = "silver";
    }
    else if(font == "Times") {
        ctx.font = "70px Times";
        ctx.fillStyle = "silver";
    }
    else if(font == "\"Courier New\"") {
        ctx.font = "70px Courier New";
        ctx.fillStyle = "silver";
    }
    else if(font == "Verdana") {
        ctx.font = "70px Verdana";
        ctx.fillStyle = "silver";
    }
    else if(font == "Courier") {
        ctx.font = "70px Courier";
        ctx.fillStyle = "silver";
    }
    else if(font == "\"Arial Narrow\"") {
        ctx.font = "70px Arial Narrow";
        ctx.fillStyle = "silver";
    }
    else if(font == "Candara") {
        ctx.font = "70px Candara";
        ctx.fillStyle = "silver";
    }
    else if(font == "Geneva") {
        ctx.font = "70px Geneva";
        ctx.fillStyle = "silver";
    }
    else if(font == "Calibri") {
        ctx.font = "70px Calibri";
        ctx.fillStyle = "silver";
    }
    else if(font == "Optima") {
        ctx.font = "70px Optima";
        ctx.fillStyle = "silver";
    }
    else if(font == "ArCambriaial") {
        ctx.font = "70px ArCambriaial";
        ctx.fillStyle = "silver";
    }
    else if(font == "Garamond") {
        ctx.font = "70px Garamond";
        ctx.fillStyle = "silver";
    }
    else if(font == "Perpetua") {
        ctx.font = "70px Perpetua";
        ctx.fillStyle = "silver";
    }
    else if(font == "Monaco") {
        ctx.font = "70px Monaco";
        ctx.fillStyle = "silver";
    }
    else if(font == "Didot") {
        ctx.font = "70px Didot";
        ctx.fillStyle = "silver";
    }
    else if(font == "\"Brush Script MT\"") {
        ctx.font = "70px Brush Script MT";
        ctx.fillStyle = "silver";
    }
    else if(font == "\"Lucida Bright\"") {
        ctx.font = "70px Lucida Bright";
        ctx.fillStyle = "silver";
    }
    else if(font == "Copperplate") {
        ctx.font = "70px Copperplate";
        ctx.fillStyle = "silver";
    }
    ctx.fillText(result[0], 30, 135);
    ctx.fillText(result[1], 30, 255);
    console.log("ctx.font is " + ctx.font);

    // console.log(font);

    // ctx.font = "200px Times New Roman";
    // console.log(ctx.font);  
}

function Download() {
    // var rand = Math.floor(Math.random() * 100000) + 1;
    // document.getElementById("btnDownload").value = rand + "";
    // console.log("rand in html is : " + $('#btnDownload').val());

    const a = document.createElement("a");

    document.body.appendChild(a);
    a.href = myCanvas.toDataURL();
    a.download = "result.png";
    a.click();
    document.body.removeChild(a);

    // var get = $('#btnDownload').val();
    // console.log("get is :" + get);
}