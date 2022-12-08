run echo_server.py and echo_client.py on 2 different terminal
change the repository path in the server and client code
client side:
enter the file name from which data to be extracted(eg. teest.txt)
the server  will open the file return the name from the file and then send all the words till EOF is reached.
the client side will create a new txt file and store all the info except the name.

server side:
readlines from the asked file
break them into words and send each word over the connection