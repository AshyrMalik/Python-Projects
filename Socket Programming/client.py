import socket

# Define the server address and port
SERVER_HOST = 'localhost'
SERVER_PORT = 12345

# Create a socket object using IPv4 and TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Define your message
message = "Hello, World!"

# 1. Determine the length of the message
L = len(message)

# 2. Pad the length with leading zeros to make it 3 characters
header = str(L).zfill(3)  # e.g., if L is 13, header becomes "013"

# 3. Concatenate the header and the message
data = header + message

# 4. Send the data to the server
client_socket.sendall(data.encode())

print("Sent:", data)

client_socket.close()
