import socket
import sys
import time
import matplotlib.pyplot as plt

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Connect the socket to the port where the server is listening
serverAddressPort   = ("127.0.0.1", 20001)
print ('starting up on %s port %s' % serverAddressPort,file=sys.stderr)

count=1
data = 0.0
rtt_list = []
num_pack_lost = 0

interval = float(sys.argv[1])#float(input("give the interval"))#0.01
pack_size = int(sys.argv[2])#int(input("give input size"))
no_packs = int(sys.argv[3])#int(input("give number of packets"))
msg = "a"*pack_size
start = 0.0
end = 0.0
throughput = []
delay =[]
while count!=16:    #nummber of times we calculate delay
    data = '88.88'
    per_delay = []
    total_data = 0
    #print("old ",old_t)
    start = time.perf_counter()
    while time.perf_counter()<start+1:
        old_t = float(time.perf_counter())
        sock.sendto(msg.encode(),serverAddressPort)
        while time.perf_counter()<old_t+0.001:
            data = sock.recvfrom(pack_size)
            new_t = float(time.perf_counter())
            if data!='88.88':
                break
        if data=='88.88':
            print('packet lost')
        else:
            total_data+=pack_size
            per_delay.append(new_t-old_t)
        time.sleep(interval)
    throughput.append(total_data)
    delay.append(sum(per_delay)/len(per_delay))
    count+=1

x = []
for i in range(1,16):
    x.append(i)
print("avg throughput:",sum(throughput)/len(throughput),"bytes")

fig,axs = plt.subplots(1,2,figsize=(15, 15))
axs[0].plot(x,throughput)
axs[0].set_title("throughput")
axs[1].plot(x,delay) 
axs[1].set_title("avg_delay")
plt.show()


# if num_pack_lost>0:
#     print('number of packet lost:',num_pack_lost)
#     print("accuracy",((no_packs-num_pack_lost)*100)/9)
# else:
#     print("no packet lost")
#     print("accuracy = 100%")

# print("========================================")
# print("average RTT: ",sum(rtt_list)/(no_packs-num_pack_lost))\

# print("========================================")
# print("maximum RTT: ",max(rtt_list))


    
  