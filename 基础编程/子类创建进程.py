from multiprocessing import Process
import time

class MyNewPrecess(Process):
    def run(self):
        print('------子进程-----')
        



print('---main----')
p=MyNewPrecess()
p.start()
p.join()   
