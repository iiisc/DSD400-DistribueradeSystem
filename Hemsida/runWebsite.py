import http.server
import socketserver

PORT = 80
PATH = "/index.html" 
#PATH = "C:/Users/Fractal ERA/Desktop/WEBSITE/index.html"
#PATH = "C:\Users\Fractal ERA\Desktop\WEBSITE\index.html"
#PATH = "C:\\Users\\Fractal ERA\\Desktop\\WEBSITE\\index.html"

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = PATH
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler
server = socketserver.TCPServer(('', PORT), Handler)

server.serve_forever()