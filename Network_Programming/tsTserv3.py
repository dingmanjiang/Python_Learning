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
        data_b = tcpCliSock.recv(BUFSIZ)
        data = data_b.decode()
        print(data,type(data))
        if not data:
            break
        data = '[%s] %s' %(ctime(), data)
        print(data, type(data))
        data_b = data.encode(encoding='utf-8')
        tcpCliSock.send(data_b)

    tcpCliSock.close()

tcpSerSock.close()

