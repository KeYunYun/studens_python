import threading

import time

def sayhello():
    print('你好')
    time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        t=threading.Thread(target=sayhello)
        t.start()
