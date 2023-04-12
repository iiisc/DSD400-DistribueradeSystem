#!/usr/bin/env python3
#
# Exempel för DSD400-kursen. Webbserver som tillhandahåller statiska
# filer från "html"-katalogen samt genererad dynamiskt JSON för
# URL:er som börjar på "/api".
#
# Thomas Lundqvist, 2020, use freely!

from http.server import SimpleHTTPRequestHandler, HTTPServer
import json, random

INTERFACES = 'localhost'
PORT = 8020

# This class will handle any incoming GET requests
# URLs starting with /api/ is catched for REST/JSON calls
# Other URLs are handled by default handler to serve static
# content (directories, files)

class RequestHandler(SimpleHTTPRequestHandler):
        
    # Override handler for GET requests
    def do_GET(self):
        if self.path.startswith('/api'):
            self.send_response(200)
            self.send_header('Content-type','text/json')
            self.end_headers()
            if self.path.startswith('/api/slump'):
                # Send the response dict as json message
                response = {'title': 'Min fina rubrik',
                            'text': 'Lite slump: ',
                            'slump': random.randint(0,100)}
            else:
                response = {'error': 'Not implemented'}
            self.wfile.write(json.dumps(response).encode())
            return
        
        # Call default serving static files if not '/api'
        # from 'html' subdirectory
        
        self.path = '/html' + self.path
        return super().do_GET()
    
try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer((INTERFACES, PORT), RequestHandler)
    print('Starting HTTP server on http://' + INTERFACES + ":" + str(PORT))
    server.serve_forever()
    
except KeyboardInterrupt:
    print('Ctrl-C received, shutting down the web server')
    server.socket.close()

