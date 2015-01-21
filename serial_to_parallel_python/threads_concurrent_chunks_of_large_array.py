#!/usr/bin/env python
# Ben Payne
# last updated 20150121
# created 20150121

# package dependencies
import sys # command line arguments
import time # pause to simulate computation delay
import multiprocessing

def worker(thread_ary,thread_indx):
  time.sleep(2)
  print("from thread index "+str(thread_indx))
  print(thread_ary)
  return thread_ary


if __name__ == '__main__':
  if (len(sys.argv) != 2):
    print("\n    ERROR: expecting 1 command line argument, number of threads,\n got "+str(len(sys.argv)-1)+" arguments\n")
    exit(1)
  num_threads=int(sys.argv[1])
  print("  number of threads: "+str(num_threads))

  pool = multiprocessing.Pool(processes=num_threads)

  num_lines=100
  # this array is all the data we want to to act on
  big_ary=range(1,num_lines+1)

  chunk_size = int(int(num_lines)/int(num_threads))

  results=[]
  for thread_indx in range(1,num_threads+1):
    start_indx = (thread_indx-1)*chunk_size
    if (thread_indx<num_threads):
      end_indx = thread_indx*chunk_size
    else: # thread_indx==num_threads
      end_indx = num_lines
#    print("start: "+str(start_indx+1)+"    end: "+str(end_indx))
    thread_ary=big_ary[start_indx:end_indx]
#    print(thread_ary) 
    results.append(pool.apply_async(worker, args=(thread_ary,thread_indx,)))
  output = []
  for p in results:
    output = output + p.get()
  print(output)
  print("done")


