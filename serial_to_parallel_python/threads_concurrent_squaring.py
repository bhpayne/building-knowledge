import time
from multiprocessing import Pool

def f(x):
    time.sleep(2)
    print(x)
    return x*x

if __name__ == '__main__':
    num_threads=10
    pool = Pool(processes=num_threads)              # start 4 worker processes
#    results = [pool.apply_async(f, args=(x,)) for x in range(1,num_threads)]
    results=[]
    for x in range(1,num_threads):
        results.append(pool.apply_async(f, args=(x,)))
    output = [p.get() for p in results]
    print(output)
    print("done")