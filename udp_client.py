# Basic Udp Client

import socket

target_host = "127.0.0.1" # expecting to change it when using according to need

target_port = 5000 # expecting to change it when using according to need

# create a socket object where AF_INET which accepts ipv4 or hostname and SOCK_DGRAM which indicates that this will be a udp client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#since udp is a connectionless protocol it doesn't need to establish a connection before sending the data, it needs host and port only when sending the data
client.sendto(b"It is a udp client", (target_host, target_port))

# receive data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()