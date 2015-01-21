import time
from multiprocessing import Pool

def f(x):
    time.sleep(2)
    print(x)
    return x*x

if __name__ == '__main__':
    num_threads=10
    pool = Pool(processes=num_threads)              # start 4 worker processes
    """
    result = pool.apply_async(f, [10])    # evaluate "f(10)" asynchronously
    print result.get()           # prints "100" unless your computer is *very* slow
    """
    """
    print pool.map(f, range(10))          # prints "[0, 1, 4,..., 81]"
    """
    results = [pool.apply_async(f, args=(x,)) for x in range(1,num_threads)]
    output = [p.get() for p in results]
    print(output)
    print("done")