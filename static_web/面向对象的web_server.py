from socket import *
from threading import Thread

class HTTPServer(object):
    ''''''
    def __init__(self,port):
        HOST = ''
        PROT = port
        BUFSIZE = 1024
        ADDR = (HOST, PROT)
        self.serSocket = socket(AF_INET, SOCK_STREAM)
        self.serSocket.bind(ADDR)


    def handle_client(self,client_socket):
        '''处理客服端请求'''
        print('连接成功')
        request_data = client_socket.recv(1024)
        print('request_data>>>%s' % request_data)
        # 响应报文
        response_start_line = 'HTTP/1.1 200 OK\r\n'
        response_headers = 'Server:My server\r\n'
        response_body = 'hello ni hao'
        respon = response_start_line + response_headers + '\r\n' + response_body
        client_socket.send(bytes(respon, 'utf-8'))
        print('respon_data>>>%s' % respon)
        client_socket.close()

    def start(self):
        self.serSocket.listen(5)
        while True:
            clientSocket, clientAddr = self.serSocket.accept();
            print(clientAddr)
            client = Thread(target=self.handle_client, args=(clientSocket,))
            client.start()
            print('start')
        self.serSocket.close()



def main():
    http_sever = HTTPServer(8000)
    http_sever.start()
if __name__=='__main__':
    main()

