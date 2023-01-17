# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:15:43 2022

@author: M01
"""

"""
Address families
AF_UNIX, AF_LOCAL : Local communication
AF_INET : IPv4 Internet protocols
AF_INET6 : IPv6 Internet protocols
AF_IPX : IPX : Novell protocols
AF_BLUETOOTH : Wireless bluetooth protocols
AF_PACKET : Low level packet interface


Network protocols
The socket.SOCK_STREAM is used to create a socket for TCP and socket.SOCK_DGRAM for UDP.
"""

import socket

def send_message(HOST, PORT, bufsize=1024, timeout=10):
    while True:
        clientMessage = str(input("Message: "))
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(timeout)
        client.connect((HOST, PORT))
    
        client.sendall(clientMessage.encode())
        
        serverMessage = str(client.recv(bufsize), encoding='ascii') # encoding: ascii, utf-8
        print('Server:', serverMessage)
        
        client.close()
        
if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 9527
    send_message(HOST, PORT)