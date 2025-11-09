import socket
import os

def send_file(filepath):
    host = '127.0.0.1'
    port = 12346
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    filename = os.path.basename(filepath)
    filename_bytes = filename.encode()
    filename_size = len(filename_bytes)
    
    # Send filename size (2 bytes) and filename
    client_socket.send(filename_size.to_bytes(2, 'big'))
    client_socket.send(filename_bytes)
    
    # Send the file content
    try:
        with open(filepath, 'rb') as f:
            while True:
                bytes_read = f.read(4096)
                if not bytes_read:
                    break
                client_socket.sendall(bytes_read)
        print("File sent successfully.")
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        
    client_socket.close()

if __name__ == "__main__":
    # Create a dummy file to send
    try:
        with open("testfile.txt", "w") as f:
            f.write("This is a test file for the CNL experiment.")
    except:
        pass # File likely already exists, which is fine
        
    filepath = "testfile.txt" # Using a local file
    send_file(filepath)