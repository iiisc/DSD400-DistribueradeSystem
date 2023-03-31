import socket
import sys
import time

#HOST = socket.gethostbyname(socket.gethostname())
#PORT = 50007
#HOST = sys.argv[1]
#PORT = int(sys.argv[2])

HOST = "127.0.0.1"
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
print(s.recv(1024).decode())
#print(s.recv(1024).decode())
     
while True:
    indata=input(" ")
        
    s.sendall(indata.encode())
    if indata == "q" or indata == "quit":
        time.sleep(0.1)
        print("-- CLIENT DYING IN A FIRE --")
        break
    data = s.recv(1024)
    data=data.decode()
        
    print(repr(data))
