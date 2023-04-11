import http.server
import socketserver

PORT = 80


class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler
server = socketserver.TCPServer(('', PORT), Handler)

server.serve_forever()