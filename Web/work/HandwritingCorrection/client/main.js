const clearButton = document.querySelector('.clear');
const stroke_weight = document.querySelector('.stroke-weight');
const color_picker = document.querySelector('.color-picker');

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
    ctx.strokeStyle = color_picker.value;

    ctx.lineTo(x - 210, y - 195); // 실제 화면상의 마우스 좌표와 캔버스가 나타나는 좌표와 다르면 갭이 생김
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x - 210, y - 195);
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