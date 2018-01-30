from socket import *
from threading import Thread

HTML_ROOT_DIR='./index.html'


def handle_client(client_socket):
    '''处理客服端请求'''
    print('连接成功')
    request_data=client_socket.recv(1024)
    print('request_data>>>%s'  %request_data)
    #响应报文
    response_start_line='HTTP/1.1 200 OK\r\n'
    response_headers='Server:My server\r\n'
    response_body='hello ni hao'
    respon=response_start_line+response_headers+'\r\n'+response_body
    client_socket.send(bytes(respon,'utf-8'))
    print('respon_data>>>%s' % respon)
    client_socket.close()

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
        print(clientAddr)
        client=Thread(target=handle_client , args=(clientSocket,))
        client.start()
        print('start')
    serSocket.close()

if __name__=='__main__':
    main()
