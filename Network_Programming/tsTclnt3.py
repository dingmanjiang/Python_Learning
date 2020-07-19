#!/usr/bin/python3

# 这个脚本创建一个tcp客户端
# 它提示用户输入发送到服务器端的消息，并接受从服务器端返回的添加了时间戳前缀的相同消息，然后将结果展示给用户。

from socket import *

# get host ip address
# 这是使用了try-except来捕捉因为输入服务器ip地址错误而产生的程序问题。
# 这里只接受一次错误输入，如果需要建立一个ip校验机制，可以专门建立一个函数接受来反复使用。
# 另外也可以在输入缓解使用政策表达式来验证地址的格式。
# todo 有空可以把这两个方式都写出来
try:
    HOST = input('Please input your server IP address: ')
    if HOST == '':
        HOST = 'localHOST'

    PORT_str = input('Please input your server port: ')
    if PORT_str == '':
        PORT_str = '21567'
    PORT = int(PORT_str)

    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
except Exception as connect_error:
    print(connect_error)
    print('The server does not exist or the IP address of the server is wrong!')
    HOST = input('Please input your server IP address again: ')
    ADDR = (HOST, PORT)
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
