from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
from multiprocessing import Process


HOST = ["212.25.133.127", "212.25.133.126"]
PORT = 50007

def client():
    print("Client körs")
    NAME = "Carl: "

    s = xmlrpc.client.ServerProxy("http://"+HOST[0]+":"+str(PORT))
    #s1 = xmlrpc.client.ServerProxy("http://"+HOST[1]+":"+str(PORT))

    while True:
        sendMsg = input("Chat: ")
        payload = NAME + sendMsg
        s.broadcast(payload)
        #s1.broadcast(payload)

p = Process(target=client)
p.start()

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer((HOST[0], PORT),
                        requestHandler=RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()

    def broadcast(msg):
        print(msg)
        return

    server.register_function(broadcast)
    server.serve_forever()




