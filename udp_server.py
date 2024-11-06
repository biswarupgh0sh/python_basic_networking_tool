# Basic Udp Server

import socket
import threading

IP = "0.0.0.0"
PORT = 5000

def main():
    # Create a udp socket
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Make the socket to listen on the desired ip and port
    server.bind((IP, PORT))
    print(f'[*] UDP Server is listening on {IP}:{PORT}')

    while True:
        # Receive the client socket in the client variable and the remote connection details in the address variable
        data, address = server.recvfrom(1024)
        print(f'[*] Received data from {address[0]}:{address[1]}')
        
        # Create a new thread everytime a client tries to connect
        client_handler = threading.Thread(target=handle_client, args=(server, data, address))
        client_handler.start()

def handle_client(server_socket, data, client_address):
    print(f'[*] Data received: {data.decode("utf-8")} from {client_address}')
    # Send a response back to the client
    server_socket.sendto(b'ACK', client_address)

if __name__ == '__main__':
    main()