#!/usr/bin/python3

# 这个脚本创建一个tcp服务器
# 它接受来自客户端的消息，并返回加了时间戳前缀的相同消息。

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' %(bytes(ctime(), 'utf-8'), data))

    tcpCliSock.close()

tcpSerSock.close()

