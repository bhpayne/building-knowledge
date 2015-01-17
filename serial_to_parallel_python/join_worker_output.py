#!/usr/bin/env python
# Ben Payne
# last updated 20150116
# created 20150116

# package dependencies
import pickle # serialize data output
import sys # command line arguments

def read_from_multiple_files(output_file_name,pkl_extension,num_cores):
  all_file_contents=[]
  for file_indx in range(1,num_cores+1):  
    pkl_file=open(output_file_name+str(file_indx)+pkl_extension,'rb') # read
    file_contents=pickle.load(pkl_file) # this is an array
    pkl_file.close()
    for value in file_contents:
      all_file_contents.append(value)
  return all_file_contents

def write_to_file(all_file_contents,pkl_file_name,dat_file_name):
  output=open(pkl_file_name,'wb')
  pickle.dump(all_file_contents,output)
  output.close()

  datfil = open(dat_file_name,'w')  
  for value in all_file_contents:
    datfil.write(str(value)+"\n")
  datfil.close()  



if (len(sys.argv) != 2):
  print("\n    ERROR: expecting 1 command line argument (number of files), got "+str(len(sys.argv)-1)+"\n")
  exit(1)
  
num_cores=int(sys.argv[1])

output_file_name='output_'
pkl_extension='.pkl'

all_file_contents=read_from_multiple_files(output_file_name,pkl_extension,num_cores)

print(all_file_contents)
pkl_file_name='output_from_joiner.pkl'
dat_file_name='output_from_joiner.dat'
write_to_file(all_file_contents,pkl_file_name,dat_file_name)

