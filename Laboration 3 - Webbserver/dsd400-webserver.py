from http.server import SimpleHTTPRequestHandler, HTTPServer
import json, random
import pymysql

INTERFACES = "212.25.133.39"
PORT = 8020

class RequestHandler(SimpleHTTPRequestHandler):
        
    # Override handler for GET requests
    def do_GET(self):
        if self.path.startswith('/api'):
            self.send_response(200)
            self.send_header('Content-type','text/json')
            self.end_headers()
            
            if self.path.startswith('/api/spelare'):
                con = pymysql.connect(
                    user="pyVACL",
                    password="lurigtpassword",
                    host="dsd400.port0.org",
                    port=3306,
                    database="VA_CL"
                )
                cur = con.cursor()
                cur.execute("SELECT * FROM Spelare")
                res = cur.fetchall()
                response = res
                con.close()
     
            else:
                response = {'error': 'Not implemented'}
            self.wfile.write(json.dumps(response).encode())
            return
            
        self.path = '/html' + self.path
        return super().do_GET()

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/json')
        self.end_headers() 
        content_len = int(self.headers['content-length'])
        post_body = self.rfile.read(content_len)
        test_data = json.loads(post_body)
        nyttid=test_data['id']
        nyttnamn= test_data['namn']
        nyalder=test_data['alder']

        query="INSERT INTO Spelare (SpelarID, Namn, Ålder) VALUES ("+str(nyttid)+", \'"+nyttnamn+"\', "+str(nyalder)+");"
        print(query)
        
        connection = pymysql.connect(
            user="pyVACL",
            password="lurigtpassword",
            host="dsd400.port0.org",
            port=3306,
            database="VA_CL"
            )

        cur = connection.cursor()
        cur.execute(query)

        connection.commit()



try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer((INTERFACES, PORT), RequestHandler)
    print('Starting HTTP server on http://' + INTERFACES + ":" + str(PORT))
    server.serve_forever()
    
except KeyboardInterrupt:
    print('Ctrl-C received, shutting down the web server')
    server.socket.close()

