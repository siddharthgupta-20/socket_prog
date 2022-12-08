import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print ('starting up on %s port %s' % server_address,file=sys.stderr)
sock.connect(server_address)

try:
    
    # Send data
    file_name =input("file name:")
    print( 'sending file name "%s"' % file_name,sys.stderr)
    sock.sendall(file_name.encode())

    # Look for the response
    # amount_received = 0
    # amount_expected = len(message)
    f = open("new_file.txt","a")
    data = ' '
    flag = 0
    while data!="EOF":
        data = sock.recv(1024).decode()
        print(data)
        if data == "error 404: file not found":
            print("file not found")
            data = "EOF"
        else:    
            
            print('recieved "%s"' % data,sys.stderr)
            if flag==0:
                sock.sendall('Word_#1'.encode())
                flag=1
            else:
                if data!="EOF":
                    f.write(data+" ")
                sock.sendall('Word_#1'.encode())
        
    f.close()
    
    

finally:
    print ( 'closing socket',sys.stderr)
    sock.close()