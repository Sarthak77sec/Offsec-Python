import socket

target_ip = "127.0.0.1"
target_port = 9997  # Port number should be an integer

# Create a socket layer
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some data
client.sendto(b"AAABBBCCC", (target_ip, target_port))

# Receive data from the host
data, addr = client.recvfrom(4096)  # Ensure buffer size is sufficient

# Decode and print the data
print(data.decode())

# Close the socket
client.close()
