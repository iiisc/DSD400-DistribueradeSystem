from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client


HOST = ["212.25.133.127"]
PORT = 1234

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer((HOST[0], PORT),
                        requestHandler=RequestHandler, allow_none=True, logRequests=False) as server:
    server.register_introspection_functions()

    def broadcast(msg):
        print(msg)
        return

    server.register_function(broadcast)    
    server.serve_forever()
        
