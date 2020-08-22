//// Not using express
// const http = require('http')
// const fs = require('fs')
// const port = 3000


// const server = http.createServer(function(req, res) {
//     res.writeHead(200,{ 'Content-Type': 'text/html' })
//     fs.readFile('index.html', function(error, data) {
//         if(error) {
//             res.writeHead(404)
//             res.write('Error: File Not Found')
//         } else {
//             res.write(data)
//         }
//         res.end()
//     })
// })

// server.listen(port, function(error){
//     if(error) {
//         console.log('Something went wrong', error)
//     } else {
//         console.log('Server is listening on port ' + port)
//     }
// })

// Using express
var express = require("express");
var app = express();
var path = require("path");

app.use('/script', express.static(__dirname + '/script')); // 필수

app.get('/',function(req,res){
  res.sendFile(path.join(__dirname +'/client/index.html'));
});

app.listen(3000);

console.log("Running at Port 3000");

function py(value) {
  const spawn = require('child_process').spawn; // require does not exist in client-side Javascript
  const process = spawn('python', ['./script1.py']);

  process.stdout.on('data', data=> {
      console.log(data.toString());
  });
  console.log(value);
  
  console.log("py function is end");
}