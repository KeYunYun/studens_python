from socket import *
import struct
import os

ipStress=input('请输入IP地址')
#port=input('请输入端口号')
fileName=input('请输入要下载的文件名')
ipAddress=(ipStress,69)


udpSocket=socket(AF_INET,SOCK_DGRAM)
requestStr=struct.pack('!H'+str(len(fileName))+'sb5sb',1,fileName.encode(),0,b'octet',0)
udpSocket.sendto(requestStr,ipAddress)

recvFile=''
resert=''
currentNum=0
recvLen=0
while True:
    recvFile=udpSocket.recvfrom(1024)[0]
    recvLen=len(recvFile)
    print(recvLen)
    recvCon, recvNum = struct.unpack('!HH', recvFile[:4])
    print(str(recvCon)+'》》》》》》》》'+str(recvNum))
    if recvCon == 3:
        if recvNum == 1:
            resert = open('附件.png', 'ab+')

        if currentNum + 1 == recvNum:
            currentNum += 1
            print(currentNum)
            print(recvFile[4:])
            resert.write(recvFile[4:])
            print("接收了第%d次数据" % currentNum)

            ackbuf = struct.pack('!HH', 4, int(recvNum))
            print(ackbuf)
            udpSocket.sendto(ackbuf, ipAddress)

        if recvLen < 516:
            print('传输完成')
            resert.close()
            udpSocket.close()
            break
    if recvCon == 5:
        print('传输有误')
        break











