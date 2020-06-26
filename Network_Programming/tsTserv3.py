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
        data_b = tcpCliSock.recv(BUFSIZ)    #收到的是bytes
        data = data_b.decode()              #解码成string
        print(data,type(data))
        if not data:
            break
        data = '[%s] %s' %(ctime(), data)
        print(data, type(data))
        data_b = data.encode(encoding='utf-8')  #将string编码成bytes
        tcpCliSock.send(data_b)                 #socket.send必须是bytes对象

    tcpCliSock.close()

# todo 关于套接字的关闭，可以采用try方式进行一种优雅的或智能的关闭，这也是目前这个程序没有完善的地方
tcpSerSock.close()

