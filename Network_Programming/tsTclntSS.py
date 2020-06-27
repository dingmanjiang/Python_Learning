#!/usr/bin/python3

# 这是一个时间戳TCP客户端，它知道如何与类似文件的socketserver类StreamRequest Handler对象通信。

from socket import *

HOST = input('Please input your server IP address: ')
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data_s = ('%s\r\n' % input('> '))
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
