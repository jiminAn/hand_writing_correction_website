var express = require("express");
var app = express();
var path = require("path");

// Want to apply an external js file path
app.use('/client', express.static(__dirname + '/client'));

app.get('/',function(req,res){
  res.sendFile(path.join(__dirname +'/index.html'));
});

app.listen(3000);

console.log("Running at Port 3000");