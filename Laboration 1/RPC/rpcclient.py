import xmlrpc.client
import sys
import time

HOST = sys.argv[1]
PORT = sys.argv[2]
s = xmlrpc.client.ServerProxy("http://"+HOST+":"+PORT)


while True:
    print(s.w())
    command = input("Kommando: ")
    if command == "quit" or command == "q":
        break
    print(s.parse(command))
    

      



















































      
