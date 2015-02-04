#!/usr/bin/env python
# Ben Payne
# last updated 20150121
# created 20150121

# package dependencies
import sys # command line arguments
import time # while loop for fixed time period
import multiprocessing
import random

def worker(survey_time_in_seconds,PDU_ID,number_of_outlets):
  timeout = time.time() + survey_time_in_seconds
  outlet_power_dic = {}
  for outlet_index in range(number_of_outlets):
    outlet_power_dic[(PDU_ID,outlet_index)]=[]

  max_power=90 # watts ### FAKE DATA ###
  found_server = False # not in use
  while True: # http://stackoverflow.com/questions/13293269/how-would-i-stop-a-while-loop-after-some-amount-of-time
    ran_out_of_survey_time = time.time() > timeout
    if found_server or ran_out_of_survey_time:
      break
    for outlet_index in range(number_of_outlets):
      # issue SNMP query to PDU_ID
#       print(str(PDU_ID)+" "+str(outlet_index))
      if (outlet_index==5 and PDU_ID==0): ### FAKE DATA ###
        value = max_power                 ### FAKE DATA ###
      else:                               ### FAKE DATA ###
        value=random.randrange(0,max_power,1) # instantaneous power for the outlet in Watts ### FAKE DATA ###

      outlet_power_dic[(PDU_ID,outlet_index)].append(value)    
  return outlet_power_dic


if __name__ == '__main__':
  if (len(sys.argv) != 2):
    print("\n    ERROR: expecting 1 command line argument, number of threads,\n got "+str(len(sys.argv)-1)+" arguments\n")
    exit(1)
  num_threads=int(sys.argv[1])
  print("  number of threads: "+str(num_threads))

  survey_time_in_seconds=1
  number_of_PDUs=4           ### FAKE DATA ###
  number_of_outlets=24

  pool = multiprocessing.Pool(processes=num_threads)

  results=[]
  for PDU_ID in range(number_of_PDUs):
    results.append(pool.apply_async(worker, args=(survey_time_in_seconds,PDU_ID,number_of_outlets,)))
#   print(results)

  full_results_dic = {}
  for p in results:
    full_results_dic.update(p.get()) # http://stackoverflow.com/questions/38987/how-can-i-merge-two-python-dictionaries-in-a-single-expression

  average_power_dic = {}
  for key in full_results_dic:
#     print(key) # currently a tuple -- PDU_ID,outlet_ID
    power_ary=full_results_dic[key] # all the power values for a specific PDU_ID/outlet_ID
    average_power=sum(power_ary)/len(power_ary)
    str_key="PDU="+str(key[0])+",outlet="+str(key[1])   # convert keys from tuple to string
    average_power_dic[str_key]=average_power

#   print(average_power_dic)

  # if one of these values is much higher than the rest, that's the node we care about
  #http://stackoverflow.com/questions/613183/python-sort-a-dictionary-by-value
  num_values=0
  top_10_ary=[]
  for w in sorted(average_power_dic, key=average_power_dic.get, reverse=True):
#     print (w+": "+str(average_power_dic[w])) # display full sorted list of dic values
    num_values=num_values+1
    if num_values<11:
      top_10_ary.append(w)

  print("\ntop 10 average power values: ")
  for indx in top_10_ary:
    print (indx+": "+str(average_power_dic[indx]))
  print(" of "+str(num_values)+" values")
  
  