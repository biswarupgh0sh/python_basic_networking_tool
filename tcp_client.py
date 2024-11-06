# Basic Tcp Client

import socket

#mentioning the target host
target_host="www.example.org" # expecting to change it when using according to need

#process the host to break into arrays divided when it see a dot  
processing_host = target_host.split(".")

# create the host without the (www) or (http://www) or (https://www) part
host = ".".join(processing_host[1:])
# mentioning the target port
target_port=80 # expecting to change it when using according to need

# create a socket object where AF_INET which accepts ipv4 or hostname and SOCK_STREAM which indicates that this will be a tcp client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

#send some data
client.send(b"GET / HTTP/1.1\r\nHOST: {}\r\n\r\n".format(host))

#receive some data
response = client.recv(4096)

print(response.decode())
client.close()