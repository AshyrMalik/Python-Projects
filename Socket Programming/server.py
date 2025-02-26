import socket

# Define the server address and port
SERVER_HOST = 'localhost'
SERVER_PORT = 12345

# Create a socket object for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")


def recvall(sock, n):
    """Helper function to receive exactly n bytes from the socket."""
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            break
        data += packet
    return data


while True:
    client_socket, client_address = server_socket.accept()
    print("Accepted connection from", client_address)

    # 1. Receive the header (first 3 characters)
    header_bytes = recvall(client_socket, 3)
    if not header_bytes:
        client_socket.close()
        continue

    header = header_bytes.decode()

    # 2. Extract the length of the message from the header
    try:
        message_length = int(header)
    except ValueError:
        print("Invalid header received!")
        client_socket.close()
        continue

    # 3. Receive the rest of the message with the given length
    message_bytes = recvall(client_socket, message_length)
    message = message_bytes.decode()

    print("Received message:", message)

    client_socket.close()
