import socket
Current_room = 0
description = [
    "You see a typical class room with a whiteboard in front of you.",
    "You are in a corridor at University West.",
    "You see a restaurant where people eat lunch."]

def parse_and_execute(command):
    global Current_room
    if command == "look" or command == "l":
        return description[Current_room]
    if command == "go east" or command == "e":
        if Current_room < 2:
            Current_room += 1
            return "You walk east!"
        return "You bump into the wall!"
    if command == "go west" or command == "w":
        if Current_room > 0:
            Current_room -= 1
            return "You walk west!"
        return "You bump into the wall!"
    if command == "help" or command == "h" or command == "?":
        return "Try looking around, go east, west, or quit!"
    return "I don't understand your command!"

def running():

    finished = 0
    welcome="Welcome to the hardest game you've ever played. GLHF yo."
    welcome = welcome.encode()
    conn.sendall(welcome)

    while not finished:
     
        with conn:
            print ('Connected by ' , addr)
            while True:
                data = conn.recv(1024)
                command = data.decode()

                if command == "quit" or command == "q":
                    print("Serverside quitting, good bye")
                    finished = 1
                    return finished
                else:
                    retur=parse_and_execute(command)
                    data=retur.encode()
                    conn.sendall(data)

HOST = "127.0.0.1"
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10) #Ettan står för hur många som kan stå i kö
    while True:
        conn, addr = s.accept() # returns new socket and addr. client
        status=running()
        if status== 1 :
            break