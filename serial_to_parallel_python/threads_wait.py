import multiprocessing
import time
import sys

def daemon():
    print 'Starting:', multiprocessing.current_process().name
    time.sleep(2)
    print 'Exiting :', multiprocessing.current_process().name

def non_daemon(indx):
    print 'Starting:', multiprocessing.current_process().name
    print(indx)
    print 'Exiting :', multiprocessing.current_process().name

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    for indx in range(4):
      n = multiprocessing.Process(name='non-daemon', target=non_daemon,args=(indx,))
      n.daemon = False

    d.start()
    time.sleep(1)
    n.start()

    d.join()
    n.join()
    print("done")