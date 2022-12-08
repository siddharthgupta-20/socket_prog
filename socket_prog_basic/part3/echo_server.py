import socket
import sys
localIP     = "127.0.0.1"

localPort   = 8000

bufferSize  = 1024

# python3 script.py localhost/ip6-localhost 8000
addrinfo = socket.getaddrinfo(sys.argv[1],sys.argv[2])

# Create a datagram socket
UDPServerSocket = socket.socket(family=addrinfo[0][0], type=socket.SOCK_DGRAM)

UDPServerSocket.bind(addrinfo[0][4])



# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

   

    # Sending a reply to client

    UDPServerSocket.sendto(message, address)