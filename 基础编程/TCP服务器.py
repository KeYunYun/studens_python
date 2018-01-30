from socket import *


HOST=''
PROT=8000
BUFSIZE=1024
ADDR=(HOST,PROT)

tcpSocketSer=socket(AF_INET,SOCK_STREAM)

tcpSocketSer.bind(ADDR)
tcpSocketSer.listen(5)

while True:
    clientSocket,clientInfo=tcpSocketSer.accept()
    print('链接成功，客户端的ip为和端口为%s'%str(clientInfo))
    while True:

        recvDate=clientSocket.recv(1024)
        if not recvDate:
            break
        print('接收到的数据为%s'%recvDate)
        data=input('>>>>>')
        clientSocket.send(data.encode())

clientSocket.close()
tcpSocketSer.close()
