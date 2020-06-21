#!/usr/bin/python3

# 这个脚本创建一个tcp客户端
# 它提示用户输入发送到服务器端的消息，并接受从服务器端返回的添加了时间戳前缀的相同消息，然后将结果展示给用户。

from socket import *

# get host ip address
HOST = input('Please input your server IP address: ')
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data_s = input('> ')
    data = data_s.encode(encoding='utf-8')  # 将string编码成bytes
    if not data:
        break
    print(data_s + ' is a ', type(data))
    tcpCliSock.send(data)                   # socket.sent必须发送bytes对象
    data = tcpCliSock.recv(BUFSIZ)
    data_s = data.decode()
    if not data_s:
        break
    print(data_s)

tcpCliSock.close()
