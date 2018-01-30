from socket import *

udpSocket=socket(AF_INET,SOCK_DGRAM)

#udpSocket.bind(('',49888))

udpSocket.sendto(b'hello',('127.0.0.1',7788))

udpSocket.close
