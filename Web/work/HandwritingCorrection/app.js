var express = require("express");
var app = express();
var path = require("path");

// var MongoClient = require('mongodb').MongoClient;
// var db;

// function connectedDB() {
//     var databaseUrl = 'mongodb://localhost:27017/testdb';

//     MongoClient.connect(databaseUrl, function(err, database) {
//         if(err) {
//             console.log(err);
//         }
//         console.log('데이터베이스에 연결됨: ' + databaseUrl);
//         db = database.db('testdb');

//         var michael = {name:'Michael', age:15, gender:'M'};
//         db.collection('testdb').insert(michael);
//     });
// }

// connectedDB();


// Want to apply an external js file path
app.use('/client', express.static(__dirname + '/client'));

// Call index.html
app.get('/',function(req,res){
    res.sendFile(path.join(__dirname +'/client/index.html'));
});

// Call main.html
app.get('/main',function(req,res){
    res.sendFile(path.join(__dirname +'/client/main.html'));
});

// Call result.html
app.get('/result',function(req,res){
    res.sendFile(path.join(__dirname +'/client/result.html'));
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
    var datanumber = req.query.data;
    console.log(req.query.data);
    console.log('Rand in JS is :' + datanumber);
 
    console.log("Python is Start");
    var spawn = require('child_process').spawn;
    py = spawn('python', ['handwriting_string_predict.py']);
    
    var dataString = '';
    
    py.stdout.on('data', function(data){
        dataString += data.toString();
        console.log(dataString + "is that");
    });

    py.stdout.on('end', function(){
        // console.log('Sum of numbers ' + dataString + ' is dataString');
        console.log(dataString);
        var result = dataString + "";
        res.send({result: result}); // 데이터를 Client로 다시 리턴해주는 역할
    });

    py.stdin.write(JSON.stringify(req.query.data)); // stdin.write의 의미 알기 이게 py 코드에 보내는 데이터임 이거 했어야함!!
    py.stdin.end(); // 이거 실행된 이후에 py.stdout.on('end') 함수로 가는 건가, 함수 호출과 비슷한 역할인지 확인

    console.log("Python is End");
});