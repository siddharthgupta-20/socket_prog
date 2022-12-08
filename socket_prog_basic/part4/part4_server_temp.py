import socket
import sys
import os

ip_addr = "127.0.0.1"
port = 8000

TCPServerObject = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
TCPServerObject.bind((ip_addr,port))
TCPServerObject.listen(100)

print("SERVER is ON!")

def list_files(connection):
    list_files = os.system("ls -al")
    connection.send(bytes(list_files,'ascii'))
    return


while True:
    TCPconn,addr = TCPServerObject.accept()
    print(f"{addr[0]} {addr[1]} is connected!")
    while True:
        TCPconn.send(b"Welcome to SID's server")
        TCPconn.recv(1024)
        TCPconn.send(b"You can do the following using the keyword given")
        TCPconn.recv(1024)
        TCPconn.send(b"'list': Show all the files in the current directory")
        TCPconn.recv(1024)
        # TCPconn.send(b"'print <filename>': Show all the files in the current directory")
        # TCPconn.recv(1024)
        TCPconn.send(b"'create <filename>': Create a new file")
        TCPconn.recv(1024)
        TCPconn.send(b"'write <filename>': Write to the file, if it already exists")
        TCPconn.recv(1024)
        TCPconn.send(b"'exit': To end this TCP connection")
        TCPconn.recv(1024)
        message = TCPconn.recv(1024).decode()
        if (message.split()[0] == "list"):
            list_files(TCPconn)
        elif (message.split()[0] == "create"):
            f = open(message.split()[1],'a')
            f.close()
            TCPconn.send(b"file created")
        elif (message.split()[0] == "write"):
            f = open(message.split()[1],'a')
            f.write(message)
            f.close()
            TCPconn.send(b"written")
        elif (message.split()[0] == "exit"):
            TCPconn.send(b"Bye from the server!")
            TCPconn.close()
            break
            