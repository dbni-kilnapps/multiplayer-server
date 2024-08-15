import socket
import threading
import sys
import os
from dotenv import load_dotenv

# Flag to signal the server to stop
stop_server = False

load_dotenv()
server_port = os.getenv('PORT')

def start_server():
    global stop_server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', int(server_port))
    server_socket.bind(server_address)
    server_socket.listen(1)
    print(f'Server is listening on port {server_address[1]}')

    while not stop_server:
        client_socket = None
        try:
            server_socket.settimeout(1.0)  # Set timeout to allow checking the stop flag
            client_socket, client_address = server_socket.accept()
            print(f'Connection from {client_address}')

            data = client_socket.recv(1024)

            # Use the received data to do something


            print(f'Received {data.decode()}')

            res = "Data received"
            client_socket.sendall(res.encode())
        except socket.timeout:
            continue
        finally:
            if client_socket:
                client_socket.close()

    server_socket.close()
    print("Server has been stopped.")

def listen_for_key():
    global stop_server
    while True:
        key = input("Press 'q' to stop the server: ")
        if key.lower() == 'q':
            stop_server = True
            break

# Create and start the server thread
server_thread = threading.Thread(target=start_server)
server_thread.start()

# Listen for the key press in the main thread
listen_for_key()

# Wait for the server thread to finish
server_thread.join()