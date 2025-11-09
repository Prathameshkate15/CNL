import socket

def receive_file():
    host = '0.0.0.0'
    port = 12346
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # --- ADD THIS LINE ---
    # This allows the socket to be reused immediately
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # ---------------------
    
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on port {port}...")
    
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Receive file name size and name
    filename_size = int.from_bytes(conn.recv(2), 'big')
    filename = conn.recv(filename_size).decode()
    print(f"Receiving file: {filename}")

    with open(f"received_{filename}", 'wb') as f:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            f.write(data)
            
    print("File received successfully.")
    conn.close()

if __name__ == "__main__":
    receive_file()