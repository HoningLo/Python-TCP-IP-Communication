# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:14:17 2022

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

def build_server(HOST, PORT, bufsize=1024):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f'server start at: {HOST}:{PORT}')
    
    while True:
        conn, addr = server.accept()
        print(f'connected by {addr}')
        clientMessage = str(conn.recv(bufsize), encoding='ascii') # encoding: ascii, utf-8
    
        print('Client message is:', clientMessage)
    
        serverMessage = f"[ECHO] {clientMessage}"
        conn.sendall(serverMessage.encode())
        conn.close()
        
if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 9527
    build_server(HOST, PORT)