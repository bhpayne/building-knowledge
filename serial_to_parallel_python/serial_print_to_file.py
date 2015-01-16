#!/usr/bin/env python
# Ben Payne
# last updated 20150116
# created 20150116

# package dependencies
import yaml # for reading parameters from file # http://pyyaml.org/wiki/PyYAML
import pickle # serialize data output
# import cPickle as pickle # "upto 1000 times faster because it is in C"

def write_to_file(num_int_to_print,pkl_file_name,dat_file_name):
  datfil = open(dat_file_name,'w')
  output=open(pkl_file_name,'wb')
  
  indx_ary=[]
  for indx in range(1,num_int_to_print+1):
    datfil.write(str(indx)+"\n")
    indx_ary.append(indx)
  pickle.dump(indx_ary,output)
  datfil.close()  
  output.close()

def read_from_file(pkl_file_name):
  pkl_file=open(pkl_file_name,'rb') # read
  file_contents=pickle.load(pkl_file)
  pkl_file.close()
  print(file_contents)

input_stream=file('parameters.input','r')
input_data=yaml.load(input_stream)
num_int_to_print=input_data["num_int_to_print"]
input_stream.close() # done reading parameters input

pkl_file_name='output.pkl'
dat_file_name='output.dat'

write_to_file(num_int_to_print,pkl_file_name,dat_file_name)
read_from_file(pkl_file_name)
