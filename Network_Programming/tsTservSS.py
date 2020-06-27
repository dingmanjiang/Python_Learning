#!/usr/bin/python3

# SockerServer时间戳TCP服务器
# 通过使用SocketServer类、TCPServer和StreamRequestHandler, 该脚本创建了一个时间戳tcp服务器。

import socketserver
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print('...connected from: ', self.client_address)
        recieve_b = self.rfile.readline().strip()
        send_s = '[%s]' % ctime() + recieve_b.decode()
        send_b = send_s.encode(encoding='utf-8')
        self.wfile.write(send_b)

tcpSerSock = socketserver.TCPServer(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpSerSock.serve_forever()
