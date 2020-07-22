#!/usr/bin/python3

# 这个脚本创建一个udp客户端
# 它提示用户输入发送到服务器端的消息，并接受从服务器端返回的添加了时间戳前缀的相同消息，然后将结果展示给用户。

from socket import *

# get host ip address
HOST = input('Please input your server IP address: ')
if HOST == '':
    HOST = 'localhost'

PORT_str = input('Please input your server port: ')
if PORT_str == '':
    PORT_str = '21568'
PORT = int(PORT_str)

BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data_s = input('> ')
    data = data_s.encode(encoding='utf-8')  # 将string编码成bytes
    if not data:
        break
#    print(data + ' is a ', type(data))
    udpCliSock.sendto(data, ADDR)                   # socket.sent必须发送bytes对象
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    data_s = data.decode()
    if not data_s:
        break
    print(data_s)

udpCliSock.close()
