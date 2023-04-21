var express = require('express');   //Require används för att ladda moduler

var app = express();                //Express är modulen
var mysql = require('mysql');


app.get('/', function(request, response) {
    response.sendFile('C:/Users/Fractal ERA/Documents/GitHub/DSD400-DistribueradeSystem/nodejs/index.html');
});

app.get('/api/spelare', function(GET, response){
    var connection = mysql.createConnection({
        user: "pyVACL",
        password: "lurigtpassword",
        host: "dsd400.port0.org",
        database: "VA_CL"
    });

    connection.connect(function(err) {
        if (err) throw err;
        connection.query("SELECT * FROM Spelare", function (err, result) {
            //if (err) throw err;
            //str = JSON.stringify(result);
            console.log(result);
            response.send(result)
        });
    });
});

app.get('/api/apa', function(request, response){
    response.send("Chimpans")
  });


var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("Server startar på address http://%s:%s", host, port)
})