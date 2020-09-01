const clearButton = document.querySelector('.clear');
const stroke_weight = document.querySelector('.stroke-weight');
const color_picker = document.querySelector('.color-picker');

const btnDownload = document.querySelector("#btnDownload"); // Download button

const myCanvas = document.querySelector('#myCanvas');
const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

let isDrawing = false;
var cnt = 0;

canvas.addEventListener('mousedown', start);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stop); 

clearButton.addEventListener('click', clearCanvas);

window.onload = function() {
    console.log("onload");
    pixel();
}


function pixel() {
    ctx.strokeStyle = "#ffffff";
    ctx.lineWidth = "1";
    ctx.beginPath();
    ctx.rect(0,0,1140,260);
    ctx.fillStyle = "white";
    ctx.fill();
    ctx.closePath();
    ctx.stroke();
    ctx.beginPath();

    // Height Pixel
    for(var i = 20; i <= 1120; i += 100) {
        ctx.strokeStyle = "#50bcdf";
        ctx.lineWidth = "1";
        ctx.beginPath();
        ctx.moveTo(i,20);
        ctx.lineTo(i,120);
        ctx.closePath();
        ctx.stroke();
        ctx.beginPath();
    }

    // Height Pixel
    for(var i = 20; i <= 1120; i += 100) {
        ctx.strokeStyle = "#50bcdf";
        ctx.lineWidth = "1";
        ctx.beginPath();
        ctx.moveTo(i,140);
        ctx.lineTo(i,240);
        ctx.closePath();
        ctx.stroke();
        ctx.beginPath();
    }

    // Width Pixel
    for(var i = 20; i <= 120; i += 100) {
        ctx.beginPath();
        ctx.moveTo(20,i);
        ctx.lineTo(1120,i);
        ctx.closePath();
        ctx.stroke();
        ctx.beginPath();
    }

    for(var i = 140; i <= 240; i += 100) {
        ctx.beginPath();
        ctx.moveTo(20,i);
        ctx.lineTo(1120,i);
        ctx.closePath();
        ctx.stroke();
        ctx.beginPath();
    }

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
    ctx.strokeStyle = "#171717";

    ctx.lineTo(x - 177, y - 107); // 실제 화면상의 마우스 좌표와 캔버스가 나타나는 좌표와 다르면 갭이 생김
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x - 177, y - 107);
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
    canvas.width = 1100 + 40;
    canvas.height = 200 + 60;
}
resizeCanvas();

function Download() {
    console.log("btndownload");
   
        const dataURI = myCanvas.toDataURL();
        sessionStorage.setItem('url', dataURI); // 미리보기 사진 보여주는 역할

        var rand = Math.floor(Math.random() * 100000) + 1;
        document.getElementById("btnDownload").value = rand + "";
        console.log("rand in html is : " + $('#btnDownload').val());

        const a = document.createElement("a");

        // document.body.appendChild(a);
        a.href = myCanvas.toDataURL();
        a.download = "example" + $('#btnDownload').val() + ".png";
        a.click();
        // document.body.removeChild(a);

        var get = $('#btnDownload').val();
        console.log("get is :" + get);

        // Ajax GET Method TEST
        $.ajax({
            url: '/api/get',
            dataType: 'json',

            type: 'GET',
            data: {data: get},
            success: function(result) {
                if(result) {
                    sessionStorage.setItem('result', result.result); // Python 코드 돌려서 나온 결과값을 넘겨줌
                    
                    // $('#get_output').html(result.result);
                    // console.log(result);
                    // console.log(result.result);
                    
                    // result : json attribute
                    // result.result : json value
                }
            }
        });
        
}

var str = '';

function getValue() { // 배열 넣고 보여주는 것까지 해야함

    // 여기서 시작할 때 애초에 변경된 스트링 파이썬 결과값도 가져올 수 있음 $이랑 저기 result하는거 잇자나

    var str = new Array();

    for(i = 0; i < 20; i++) {
        if(checkValue[i].checked === true) {
        //   str += checkValue[i].value + " ";
            str.push(checkValue[i].value);
        }
    }
    // alert(str);
    console.log(str);

    $('#getFontList').html(str);

    // document.getElementById("demo").innerHTML = ""; // 태그 초기화

    // str.forEach(function(element) {
    //     document.getElementById("demo").innerHTML += "<button id=\"fontButton\" onclick=\"setFont()\"" + ">" + element + "</button><br>";
    // });

    sessionStorage.setItem('array', str); // local보다는 session 사용
    console.log(sessionStorage.getItem('result'));
    str = '';

    location.href = "/result"; // result.html로 이동
}