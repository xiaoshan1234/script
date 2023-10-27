from socket import *

HOST = 'riverfisher.vicp.io'
PORT = 49199
BUFFSIZE = 1024
ADDRESS = (HOST, PORT)

tcpClientSocket = socket(AF_INET, SOCK_STREAM)
tcpClientSocket.connect(ADDRESS)

cmd = "ipv6"

while True:
    # 发送数据
    tcpClientSocket.send(cmd.encode('utf-8'))
    # 接收数据
    data, ADDR = tcpClientSocket.recvfrom(BUFFSIZE)
    if data.decode() != '':
        print("服务器端响应：", data.decode('utf-8'))
        break
    
tcpClientSocket.close()
print("链接已断开！")