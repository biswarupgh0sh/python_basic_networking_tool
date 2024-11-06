# Basic Tcp Server

import socket 
import threading

IP = "0.0.0.0"
PORT = 5000

def main():
    # Create a tcp socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Make the socket to listen on the desired ip and port
    server.bind((IP, PORT))
    # Listen to a maximum backlog of connections set to 5
    server.listen(5)
    print(f'[*] TCP Server is listening on { IP }:{ PORT }')

    while True:
        # Receive the client socket in the client variable and the remote connection details in the address variable
        client, address = server.accept()
        print(f'[*] Accepted connection from { address[0] }:{ address[1] }')

        # Create a new thread everytime a client tries to connect
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Request received from { request.decode("utf-8")}')
        # Send a response back to the client
        sock.send(b'ACK')

if __name__ == '__main__':
    main()
