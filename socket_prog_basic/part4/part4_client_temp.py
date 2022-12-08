import socket
import sys

ip_addr = "127.0.0.1"
port = 3000


TCPClientObject = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

TCPClientObject.connect((sys.argv[1],int(sys.argv[2])))


while True:
    starting_message1 = TCPClientObject.recv(1024)
    TCPClientObject.send(b"received")
    starting_message2 = TCPClientObject.recv(1024)
    TCPClientObject.send(b"received")
    # starting_message3 = TCPClientObject.recv(1024)
    # TCPClientObject.send(b"received")
    starting_message4 = TCPClientObject.recv(1024)
    TCPClientObject.send(b"received")
    starting_message5 = TCPClientObject.recv(1024)
    TCPClientObject.send(b"received")
    starting_message6 = TCPClientObject.recv(1024)
    TCPClientObject.send(b"received")
    starting_message7 = TCPClientObject.recv(1024)
    TCPClientObject.send(b"received")
    print(starting_message1.decode())
    print(starting_message2.decode())
    # print(starting_message3.decode())
    print(starting_message4.decode())
    print(starting_message5.decode())
    print(starting_message6.decode())
    print(starting_message7.decode())

    command = input("Enter your command: ")
    TCPClientObject.send(bytes(command,'ascii'))
    response = TCPClientObject.recv(1024)
    print("====== RESPONSE =====")
    print(response.decode())
    if (command == "exit"):
        break
print("Client exiting")