
from socket import *
from threading import Thread
import re

HTML_ROOT_DIR='./html'


def handle_client(client_socket):
    '''处理客服端请求'''
    request_data=client_socket.recv(1024)
    print('request_data>>>%s'  %request_data)
    #响应报文
    #解析报文
    request_lines=request_data.splitlines()
    for line in request_lines:
        print(line)
    request_start_line=request_lines[0]
    #提取用户要提取的文件名
    file_name=re.match(r"\w+ +(/[^ ]*) ",request_start_line.decode('utf_8')).group(1)

    #打开文件，读取内容
    try:
        file=open(HTML_ROOT_DIR+file_name,'rb')
    except IOError:
        responseHeaderLines = "HTTP/1.1 404 Not Found\r\n"
        responseBody = '文件没有找到'
    else:
        file_date=file.read()
        file.close()

        #构造响应数据
        responseHeaderLines = "HTTP/1.1 200 OK\r\n"
        responseHeaderLines += "\r\n"
        responseBody = file_date.decode("utf-8")

    response = responseHeaderLines + responseBody
    client_socket.send(bytes(response,'utf-8'))


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
