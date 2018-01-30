from  socket import *
from threading import Thread

def recvInfo(clientSocket,clientAddr):
    while True:
        print('链接成功%s' % str(clientAddr))
        recvdata = clientSocket.recv(1024)
        if not recvdata:
            break
        print(recvdata.decode())
    clientSocket.close()

    def recvInfo(clientSocket):
        while True:
            senddata=input('>>>>')
            clientSocket.send(senddata.encode())
        clientSocket.close()


def main():
    HOST = ''
    PROT = 8000
    BUFSIZE = 1024
    ADDR = (HOST, PROT)
    serSocket=socket(AF_INET,SOCK_STREAM)
    serSocket.bind(ADDR)
    serSocket.listen(5)
    while True:
        clientSocket,clientAddr = serSocket.accept();
        client=Thread(target=recvInfo,args=(clientSocket,clientAddr))
        client.start()
    serSocket.close()

if __name__=='__main__':
    main()