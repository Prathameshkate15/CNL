#run with 5.1 + 5.2

import socket

def start_client():
    host = '127.0.0.1' # Localhost
    port = 12345
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    # Send hello to server
    client_socket.sendall("Hello from client!".encode())
    
    # Receive hello back
    data = client_socket.recv(1024).decode()
    print(f"Received from server: {data}")
    
    client_socket.close()

if __name__ == "__main__":
    start_client()