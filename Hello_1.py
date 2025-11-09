import socket

def start_server():
    host = '0.0.0.0' # Listen on all interfaces
    port = 12345
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on port {port}...")
    
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    
    # Receive hello from client
    data = conn.recv(1024).decode()
    print(f"Received from client: {data}")
    
    # Send hello back
    conn.sendall("Hello from server!".encode())
    conn.close()

if __name__ == "__main__":
    start_server()