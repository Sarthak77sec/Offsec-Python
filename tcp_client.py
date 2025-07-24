import socket

server_ip = "127.0.0.1"  # Replace with the server's IP if not local
server_port = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))
client.send(b"Hello, hello there")
response = client.recv(4096)
print(response.decode())
client.close()
