import threading
from multiprocessing import Queue
from lxml import etree
import json

class ThreadCrawl(threading.Thread):
    def __init__(self):
        

def main():
    #页码的队列，表示10个页面
    pageQueue=Queue(10)
    #放入1-10的数字，先进先出
    for i in range(1,11):
        pageQueue.put(i)
    #采集结果
    dataQueue=Queue()

    #三个采集线程的名字
    crawList=["采集线程一号","采集线程二号","采集线程二号"]

    #存储三个采集线程
    threadcrowl=[]
    for threadName in crawList:
        thread=ThreadCrawl

if __name__=="__naim__":
    main()