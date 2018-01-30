from socket import *

tcpClientSocket=socket(AF_INET,SOCK_STREAM)

HOST='192.168.112.1'
PROT=8080
BUFSIZE=1024
ADDR=(HOST,PROT)

tcpClientSocket.connect(ADDR)
print('链接成功')

while True:
    data=input('>>>')
    if not data:
        break
    tcpClientSocket.send(data.encode())#发送
    data=tcpClientSocket.recv(1024)#接收
    if not data:
        break
    print(data)
tcpClientSocket.close()