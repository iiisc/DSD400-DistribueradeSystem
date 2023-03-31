import xmlrpc.client
import sys
import time

#HOST = sys.argv[1]
#PORT = sys.argv[2]

HOST = "127.0.0.1"
PORT = 1234
s = xmlrpc.client.ServerProxy("http://"+HOST+":"+str(PORT))

print(s.w())

while True:
    command = input("Kommando: ")
    if command == "quit" or command == "q":
        break
    print(s.parse(command))
    

      



















































      
