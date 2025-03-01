import socket

SERVER_HOST = 'localhost'
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

message = "Hello, World!"

L = len(message)

header = str(L).zfill(3)

data = header + message

client_socket.sendall(data.encode())

print("Sent:", data)

client_socket.close()
