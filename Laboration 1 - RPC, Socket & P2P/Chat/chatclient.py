from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client


HOST = ["212.25.133.127", "212.25.133.154", "212.25.133.155"]
PORT = [1234, 1234, 1234] 
NAME = "Haxx0rs^: "

s0 = xmlrpc.client.ServerProxy("http://"+HOST[0]+":"+str(PORT[0]))
s1 = xmlrpc.client.ServerProxy("http://"+HOST[1]+":"+str(PORT[1]))
s2 = xmlrpc.client.ServerProxy("http://"+HOST[2]+":"+str(PORT[2]))


while True:
    sendMsg = input("Chat: ")
    payload = NAME + sendMsg
    s0.broadcast(payload) ## KLAR ##
    s1.broadcast(payload) ## KLAR ## 
    s2.broadcast(payload) ## KLAR ## 

