# https://docs.python.org/2/library/multiprocessing.html
from multiprocessing import Process
import os
import time

def info(title):
    print ("\n"+title)
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print('process id: '+ str(os.getpid()))

def worker(name):
    info("worker")
    time.sleep(2)
    print("hello from "+name)

if __name__ == '__main__':
    info('main line')
    for indx in range(4):
      p = Process(target=worker, args=(str(indx),))
      p.start()
      p.join()