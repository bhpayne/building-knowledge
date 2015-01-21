#!/usr/bin/env python
# Ben Payne
# last updated 20150121
# created 20150121

# package dependencies
import yaml # for reading parameters from file # http://pyyaml.org/wiki/PyYAML
import pickle # serialize data output
import sys # command line arguments
import time # pause to simulate computation delay
import multiprocessing

def worker(num):
    """thread worker function"""
    time.sleep(2)
    print("Hello from worker "+str(num))
    return

def write_to_file(start_indx,end_indx,pkl_file_name,dat_file_name):
  datfil = open(dat_file_name,'w')
  output=open(pkl_file_name,'wb')
  
  indx_ary=[]
  for indx in range(start_indx,end_indx+1):
    datfil.write(str(indx)+"\n")
    indx_ary.append(indx)
  pickle.dump(indx_ary,output)
  datfil.close()  
  output.close()

input_stream=file('parameters.input','r')
input_data=yaml.load(input_stream)
num_int_to_print=input_data["num_int_to_print"]
input_stream.close() # done reading parameters input

if (len(sys.argv) != 3):
  print("\n    ERROR: expecting 2 command line arguments (core index, number of cores),\n got "+str(len(sys.argv)-1)+"\n")
  exit(1)
  
core_indx=int(sys.argv[1])
num_cores=int(sys.argv[2])
print("core index: "+str(core_indx)+"  number of cores: "+str(num_cores))

chunk_size = int(int(num_int_to_print)/int(num_cores))
start_indx = (core_indx-1)*chunk_size+1
if (core_indx<num_cores):
  end_indx = core_indx*chunk_size
else: # core_indx==num_cores
  end_indx = num_int_to_print

print("start: "+str(start_indx)+"    end: "+str(end_indx))

output_file_name='output_'
pkl_extension='.pkl'

pkl_file_name=output_file_name+str(core_indx)+pkl_extension
dat_file_name=output_file_name+str(core_indx)+'.dat'

time.sleep(5) # delay the process to act as computation
write_to_file(start_indx,end_indx,pkl_file_name,dat_file_name)




if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
    print(jobs)