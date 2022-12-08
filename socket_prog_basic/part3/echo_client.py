import socket
import sys
import time

addrinfo = socket.getaddrinfo(sys.argv[1],sys.argv[2])
# Create a TCP/IP socket
sock = socket.socket(family=addrinfo[0][0], type=socket.SOCK_DGRAM)

# Connect the socket to the port where the server is listening
serverAddressPort   = addrinfo[0][4]
#print ('starting up on %s port %s' % serverAddressPort,file=sys.stderr)

count=0
data = 0.0
rtt_list = []
num_pack_lost = 0

interval = float(input("give the interval"))#0.01
pack_size = int(input("give input size"))
no_packs = int(input("give number of packets"))
msg = "a"*pack_size
while count!=no_packs:
    data = '88.88'
    sock.sendto(msg.encode(),serverAddressPort)
    old_t = float(time.perf_counter())
    #print("old ",old_t)
    while time.perf_counter()<old_t+0.01:
        data = sock.recvfrom(pack_size)
        new_t = float(time.perf_counter())
        if data!='88.88':
            break
    if data=='88.88':
        print('packet lost')
        num_pack_lost+=1
    else:
        rtt = float(new_t-old_t)
        rtt_list.append(rtt)
        print("ping to site 127.0.0.1","RTT:",rtt)
    
    time.sleep(interval)
    
    count+=1


if num_pack_lost>0:
    print('number of packet lost:',num_pack_lost)
    print("accuracy",((no_packs-num_pack_lost)*100)/9)
else:
    print("no packet lost")
    print("accuracy = 100%")

print("========================================")
print("average RTT: ",sum(rtt_list)/(no_packs-num_pack_lost))\

print("========================================")
print("maximum RTT: ",max(rtt_list))


    
    # # Send data
    # file_name =input()
    # print( 'sending file name "%s"' % file_name,sys.stderr)
    # sock.sendall(file_name.encode())

    # # Look for the response
    # # amount_received = 0
    # # amount_expected = len(message)
    # f = open("new_file.txt","a")
    # data = ' '
    # flag = 0
    # while data!="EOF":
    #     data = sock.recv(1024).decode()
    #     print(data)
    #     if data == "error 404: file not found":
    #         print("file not found")
    #         data = "EOF"
    #     else:    
            
    #         print('recieved "%s"' % data,sys.stderr)
    #         if flag==0:
    #             sock.sendall('Word_#1'.encode())
    #             flag=1
    #         else:
    #             if data!="EOF":
    #                 f.write(data+" ")
    #             sock.sendall('Word_#1'.encode())
        
    # f.close()
    
    

# finally:
#     print ( 'closing socket',sys.stderr)
#     sock.close()