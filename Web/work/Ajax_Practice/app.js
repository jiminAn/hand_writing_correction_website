var express = require("express");
var app = express();
var path = require("path");

// Want to apply an external js file path
app.use('/script', express.static(__dirname + '/script'));

app.get('/',function(req,res){
  res.sendFile(path.join(__dirname +'/index.html'));
});

app.listen(3000);

console.log("Running at Port 3000");


// Ajax GET METHOD
app.get('/api/get', function(req, res) {

    // var data = req.query.data;
    // console.log('GET Parameter = ' + data); // data = GET METHOD CALL
    
    // var result = data + ' Success';
    // console.log(result);

    // res.send({result:result});

    // Python   
    console.log("Python is Start");
    var spawn = require('child_process').spawn;
    py = spawn('python', ['compute_input.py']);
    data = [1,2,3,4,5,6,7,8,9];
    dataString = '';

    py.stdout.on('data', function(data){
        dataString += data.toString();
    });
    py.stdout.on('end', function(){
        console.log('Sum of numbers=',dataString);
        res.send({result:dataString});
    });

    py.stdin.write(JSON.stringify(data)); // stdin.write의 의미 알기
    py.stdin.end(); // 이거 실행된 이후에 py.stdout.on('end') 함수로 가는 건가, 함수 호출과 비슷한 역할인지 확인

    console.log("Python is End");
});

//AJAX POST METHOD
app.post('/api/post', function(req, res){
    var data = req.body.data; // 500 Internal Server Error... Why?
    console.log('POST Parameter = ' + data);
    var result = data + ' Success';
    console.log(result);
    res.send({result:result});
});
