#!/usr/bin/python3

# 这个脚本创建一个udp服务器
# 它接受来自客户端的消息，并返回加了时间戳前缀的相同消息。

from socket import *
from time import ctime

HOST = ''
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message...')
    data_b, addr = udpSerSock.recvfrom(BUFSIZ)
    data_s = data_b.decode()  # 解码成string
    print(addr, 'send me: ',data_s)
    data_s = '[%s] %s' %(ctime(), data_s)
    data_b = data_s.encode(encoding='utf-8')  # 将string编码成bytes
    udpSerSock.sendto(data_b, addr)

# todo 关于套接字的关闭，可以采用try方式进行一种优雅的或智能的关闭，这也是目前这个程序没有完善的地方
udpSerSock.close()

