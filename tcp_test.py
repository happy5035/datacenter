# -*- coding: utf-8 -*-
from socket import *

host = '192.168.11.254'
port = 8080
addr = (host, port)
bufsize = 1024

tcpClient = socket(AF_INET, SOCK_STREAM)  # 这里的参数和UDP不一样。
tcpClient.connect(addr)  # 由于tcp三次握手机制，需要先连接
# data = bytes().fromhex('fe0700000201ff')
# tcpClient.send(data)
while True:
    print(tcpClient.recv(1))
