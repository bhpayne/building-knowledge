# http://pymotw.com/2/multiprocessing/basics.html
import time
import multiprocessing

def worker(num):
    """thread worker function"""
    time.sleep(2)
    print("Hello from worker "+str(num))
    
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
    p.join()
    print(jobs)
