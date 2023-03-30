"USAGE: echoserver.py <port>"
from socket import *    # import *, but we'll avoid name conflict
import sys

def handleClient(sock):
    print("Inside handleClient")
    data = sock.recv(32)
    while data:
        print("inside while data")
        sock.sendall(data)
        data = sock.recv(32)
    sock.close()


sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('',int(sys.argv[1])))
sock.listen(5)
while 1:    # Run until cancelled
    newsock, client_addr = sock.accept()
    print("Client connected:", client_addr)
    handleClient(newsock)