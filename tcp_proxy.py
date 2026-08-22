import sys
import socket
import threading

HEX_FILTER=''.join(
    [(len(repr(chr(i)))==3) and chr (i) or '.'
     for i in range(256)]
)

def hexdump(src,length=16,show=True):
    if isinstance(src,bytes):
        src=src.decode()

        results= list()
    for i in range(0,len(src),length):
        word=str(src[i:i+length])
        printable=word.translate(HEX_FILTER)

        hexa=' '.join([f'{ord(c)}:02X' for c in word])
        hexwidth=length*3
        results.append(f'{i:04x} {hexa:<{hexwidth}} {printable}')
        if show:# if user wants to see data show it
            for line in results:
                print(line)
            else:
                return results
#function for recieve connection
def recieve_from(connection):
    buffer=b""
    connection.settimeout(5)
    try:
        while True:
            data=connection.recv(4096)
            if not data:
                break 
            buffer += data
    except Exception as e:
        pass
    return buffer
def request_handler(buffer):
    #perform packet modification
    return buffer

def response_handler(buffer):
    #perform packer modifiction
    return buffer

def proxy_handler(client_socket,remote_host,remote_port,recieve_first):
    remote_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    remote_socket.connect((remote_host,remote_port))

    if recieve_first:
        remote_buffer=recieve_from(remote_socket)
        hexdump(remote_buffer)
    else:
        remote_buffer=b""

    remote_buffer=response_handler(remote_buffer)
    if len(remote_buffer):
        print("[<==] sending %d bytes to localhost." % len(remote_buffer))
        client_socket.sendall(remote_buffer)

    while True:
        local_buffer=recieve_from(client_socket)
        if len(local_buffer):
            print('[==>] recieved %d from localhost.' % len(local_buffer))
            hexdump(local_buffer)
            local_buffer=request_handler(local_buffer)
            if len(local_buffer):
                remote_socket.sendall(local_buffer)
                print('[==>] sent to remote.')

        remote_buffer=recieve_from(remote_socket)
        if len(remote_buffer):
            print('[<==] recieved %d from remote.' % len(remote_buffer))
            hexdump(remote_buffer)
            remote_buffer=response_handler(remote_buffer)
            if len(remote_buffer):
                client_socket.sendall(remote_buffer)
                print('[<==] sent to localhost.')

        if not len(local_buffer) and not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            break
