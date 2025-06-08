import socket
target_ip="192.168.1.2"
target_port=9997

#create a socket layer
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# send some data
client.sendto(b"AAABBBCCC",(target_ip,target_port))

# recieve data from the host 
data,addr=client.recvfrom(4096)

print(data.decode())
client.close()