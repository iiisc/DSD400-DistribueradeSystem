var express = require('express');   //Require används för att ladda moduler
var app = express();                //Express är modulen

var mysql = require('mysql');

//app.get('/', function (req, res) {
//   res.send('Hello World');
//})

//msg = "Hello world";
app.get('/', function(request, response){

    var connection = mysql.createConnection({
        user: "pyVACL",
        password: "lurigtpassword",
        host: "dsd400.port0.org",
        //port: 3306,
        database: "VA_CL"
    });

    connection.connect(function(err) {
        if (err) throw err;
        connection.query("SELECT * FROM Spelare", function (err, result, fields) {
            if (err) throw err;
            console.log(result);
        });
    });
    response.send("hemsida")
});

app.get('/api/apa', function(request, response){
    response.send("Chimpans")
  });


var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("Server startar på address http://%s:%s", host, port)
})