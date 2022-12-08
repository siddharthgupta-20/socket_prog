import socket
import sys
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind the socket to the port
server_address = ('localhost', 10000)
print ('starting up on %s port %s' % server_address,file=sys.stderr)
sock.bind(server_address) 


# Listen for incoming connections
sock.listen(1)
lst = os.listdir("D:\STUDY\CN301")
while True:
    # Wait for a connection
    print('waiting for a connection',file=sys.stderr)
    connection, client_address = sock.accept()
    count = 1
    try:
        print('connection from', client_address,file=sys.stderr)
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16).decode()
            if data.strip() in lst or data.strip()[:4] == "Word":
                if data.strip()[:4] == "Word":
                    try:
                        word1 = lines.split()[count]
                        print(word1)
                        count+=1
                        connection.send(word1.encode())
                    except:
                        break
                else:
                    print("file found. sending data")
                    temp =open(data, "r")
                    lines = temp.readline()
                    print(lines.split())
                    name = lines.split()[0]
                    connection.send(lines.encode())

                # for line in temp.readlines():
                #     connection.sendall(line.encode())
            else:
                print("file not found")
                connection.sendall("error 404: file not found".encode())
            
    finally:
        # Clean up the connection
        connection.close()