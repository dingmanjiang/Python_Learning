#!/usr/bin/python3

# 这个脚本创建一个tcp客户端
# 它提示用户输入发送到服务器端的消息，并接受从服务器端返回的添加了时间戳前缀的相同消息，然后将结果展示给用户。

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data

tcpCliSock.close()
