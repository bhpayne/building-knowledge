#!/opt/local/bin/python
# Cognitive Computing Challenge
# entry of queries

import sys
import time
import os
import datetime
from redis import Redis
redis_client=Redis()
import yaml # used to read "config.input"
import re

# connect to local Redis DB
redis_client=Redis(host='127.0.0.1', port=6379, db = 0)

# https://yaml-online-parser.appspot.com/
input_stream=file('config.input','r')
input_data=yaml.load(input_stream)
path_to_PDFs=input_data["path_to_PDFs"]



path_to_dirs=path_to_PDFs+'content_extracted_from_documents/'
list_of_dir=os.listdir(path_to_dirs)
#finds all of the keys for the dictionary in the pdf... Needs a little work 



def input_tuple_search(this_tuple):
    lst = []
    counter =0
    for i in redis_client.keys(): # this fails if Redis isn't available to connect to
        try:
            if this_tuple[0] in redis_client.hkeys(i):
                strng=redis_client.hmget(i,this_tuple[0])[0].strip()
                strng2=this_tuple[2]
                if eval(repr(strng) +this_tuple[1] + repr(strng2)):
                    counter +=1
                    #print strng,i
                    lst.append(i)
            else:
                search(tuple[0])
                
        except:
            pass
        
    return lst


def description_search(regex_string):
    filename_list=[]
    
    for this_dir in list_of_dir:
      filename=path_to_dirs+this_dir+"/pdftotext.txt"
      f=open(filename,"r")
      data=f.read()
      for lst in redis_client.hmget(this_dir,'Description'):
        for elements in re.split('\,|\.|\s\s+|&|and',str(lst).strip()):
          match =re.findall(regex_string,elements.strip())
          if match:
            #print elements.strip()
            filename_list.append(this_dir)
    return filename_list
          
          
        


d=dict()
def setfunc(d):    
    strng=''
    for key in d.keys():
        strng+=str(set(d[key]))+'&'
    return eval(strng[:-1])

def parse_input(lst=[[]]):
    if len(lst)==0:
        f1=''
        f2=''
        f3=''
        count = 0 
        d =dict()
        while f1 != 'done':
            f1=raw_input()
            if f1 == 'done':
                return setfunc(d)
            f2=raw_input()
            if f2 == 'done':
                return setfunc(d)
            elif f2== 'has':
                d[count]=description_search(f1)
                count +=1
            f3=raw_input()
            if f3 == 'done':
                return setfunc(d)
            d[count]=input_tuple_search((f1,f2,f3))
            count +=1
    else:
        d=dict()
        for indx,lsts in enumerate(lst):
            
                
            if lsts[0]!='has':
                d[indx]=input_tuple_search((lsts[0],lsts[1],lsts[2]))
            else:
                d[indx]=description_search(lsts[1])
                #print d
        return setfunc(d)

    

def clear_screen():
  os.system('cls') #for window
  os.system('clear') #for Linux

def exit_from_program():
  print("-->  Exiting")
  exit(0)

def get_text_input(prompt_text):
  text_provided=False
  while(not text_provided):
    input_text=raw_input(prompt_text)
    if (input_text==''):
      text_provided=False
      print("--> invalid input (empty); Enter a string")
    else:
      text_provided=True
  return input_text
  
def get_numeric_input(prompt_text,default_choice):
  number_provided=False
  while(not number_provided):
    input_number=raw_input(prompt_text)
    if (input_number==''):
      print("\n--> no input; defaulting")
      number_provided=True
      input_number=default_choice
    try:
      print(int(input_number))
      number_provided=True
    except ValueError:
      print("\n--> invalid choice - not an integer; try again")
  return input_number

def field_choice(fields):
    clear_screen()
    indx=0
    for dic_entry in fields:
      indx=indx+1
      print(str(indx)+"  "+dic_entry["field_name"])
#     print("0  exit")
    field_choice_indx=get_numeric_input('selection [1]: ','1')

    if ((int(field_choice_indx)>0) and (int(field_choice_indx)<=len(fields))):
#       print("selected ")
#       print(fields[int(field_choice_indx)-1])
#       time.sleep(2)
      invalid_choice=False
    else:
      print("\n--> invalid choice - integer is out of range; try again")
      time.sleep(1)
    return fields[int(field_choice_indx)-1]

def value_choice(chosen_dic):
    clear_screen()
    print("for "+chosen_dic["field_name"]+", value:")
    if   (chosen_dic["field_type"]=="text"):
      chosen_value = get_text_input(chosen_dic["field_type"]+' input: ')
    elif (chosen_dic["field_type"]=="numeric"):
      chosen_value = get_numeric_input('number [1]: ','1')
    elif (chosen_dic["field_type"]=="date"):
      valid_date=False
      while(not valid_date):
        chosen_value = get_text_input(chosen_dic["field_type"]+' input [YYYY-MM-DD]: ')
        try:
          [year,month,day]=chosen_value.split('-')
        except ValueError:
          valid_date=False
        try:
          newdate = datetime.datetime(int(year),int(month),int(day)) # don't return this
          valid_date = True
        except ValueError:
          valid_date = False

    elif (chosen_dic["field_type"]=="phone"):
      valid_phone=False
      while(not valid_phone):
        chosen_value = get_text_input(chosen_dic["field_type"]+' input [000-000-0000]: ')
        try:
          [areacode,first3,last4]=chosen_value.split('-')
          valid_phone=True
        except ValueError:
          valid_phone=False  
        if ((areacode<1000) and (first3<1000) and (last4<10000)):
          valid_phone=True      
    elif (chosen_dic["field_type"]=="unit"):
      for indx,entry in enumerate(chosen_dic["values"]):
        print(str(indx)+"   "+entry)
      user_choice= get_numeric_input('selection [0]: ','0')
      chosen_value=chosen_dic["values"][int(user_choice)]
    else:
      print("ERROR: unknown field_type")
      print(  chosen_dic["field_type"])
      exit_from_program()
    return chosen_value
  
def relation_choice(chosen_dic,numeric_relation_types,text_relation_types):
    clear_screen()
    print("for "+chosen_dic["field_name"]+", select a relation:")
    if   (chosen_dic["field_type"]=="text"):
      indx=0
      for entry in text_relation_types:
        indx=indx+1
        print(str(indx)+"  "+entry) # contains or does not contain  
      user_input = get_numeric_input('selection [1]: ','1')
      print(text_relation_types)
      chosen_relation=text_relation_types[int(user_input)-1]
    elif (chosen_dic["field_type"]=="numeric" or chosen_dic["field_type"]=="date"):
      indx=0
      for entry in numeric_relation_types:
        indx=indx+1
        print(str(indx)+"  "+entry) # <,>,==,!=,<=,>=
      user_input = get_numeric_input('selection [0]: ','0')
      chosen_relation=numeric_relation_types[int(user_input)-1]
    elif (chosen_dic["field_type"]=="phone"):
      valid_input=False
      while(not valid_input):
        print("1   is")
        print("2   is not")
        user_input = get_numeric_input('selection [1]: ','1')
        if (user_input=="1"):
          chosen_relation="=="
          valid_input=True
        elif  (user_input=="2"):
          chosen_relation="not equal to"
          valid_input=True
        else: 
          print("--> input out of range")
          valid_input=False
          
    elif (chosen_dic["field_type"]=="unit"):
      chosen_relation="equal to" # no user choice here
    else:
      print("ERROR: unknown field_type")
      print(  chosen_dic["field_type"])
      exit_from_program()
    return chosen_relation

def append_constraint():
#     clear_screen()
    print("1   finished with query constraints, continue on to construct result constraint")
    print("2   append another query constraint")
    valid_input=False
    while(not valid_input):
      user_input = get_numeric_input('\nselection [1]: ','1')
      if (user_input=='1'):
        finished_with_query_entry=True
        valid_input=True
      elif (user_input=='2'):
        finished_with_query_entry=False
        valid_input=True
      else:
        print("invalid input")
        valid_input=False
    return finished_with_query_entry

def user_choose_output_qualifier(output_qualifiers):
  clear_screen()
  print("Choose output qualifier\n")
  valid_input=False
  while(not valid_input):
    for indx,qual in enumerate(output_qualifiers):
      print(str(indx)+"   "+qual)
    ###qual_choice=get_numeric_input('selection [0]: ','0')
    qual_choice='0' ###
    valid_input=True
    output_qualifier=output_qualifiers[int(qual_choice)]
  return output_qualifier

def standard_field_or_other_entry():
  standard_field_boolean=True
  valid_input=False
  while(not valid_input):
    print("0   construct query from defined fields")
    print("1   supply query text")
    qual_choice=get_numeric_input('selection [0]: ','0')
    valid_input=True
    if ( int(qual_choice)==0 ):
      standard_field_boolean=True
    if ( int(qual_choice)==1 ):
      standard_field_boolean=False
  return standard_field_boolean

def user_defined_query():
  input_tuples_list=[]
  ###input_tuples_list.append("user-defined")
  ###input_1=get_text_input('input 1 of 2: ')
  input_1='has'
  input_2=get_text_input('input 1 of 1: ')
  ###input_3=get_text_input('input 3 of 3: ')
  input_tuples_list.append(input_1)
  input_tuples_list.append(input_2)
  ###input_tuples_list.append(input_3)
  return input_tuples_list

def user_prompt(fields,numeric_relation_types,text_relation_types,output_qualifiers,numeric_list_operations):
  print("Construct a query")
  finished_with_query_entry=False
  input_tuples_list=[]
  while(not finished_with_query_entry):
    this_query_tuple=[]
    standard_field_boolean=standard_field_or_other_entry()
    if (not standard_field_boolean):
      input_tuples_list.append(user_defined_query())            ###mike changed this field .append
    else: 
      chosen_dic     =field_choice(fields)  # field
      chosen_relation=relation_choice(chosen_dic,numeric_relation_types,text_relation_types) # relation
      chosen_value   =value_choice(   chosen_dic) # value
      ###this_query_tuple.append("defined field")
      this_query_tuple.append(chosen_dic["field_name"])
      this_query_tuple.append(chosen_relation)
      this_query_tuple.append(chosen_value)
      input_tuples_list.append(this_query_tuple)
    clear_screen()
    print("current query input:")
    print(input_tuples_list)
#     time.sleep(3)
    print("\nAppend another constraint?")
    finished_with_query_entry=append_constraint()
  output_qualifier=user_choose_output_qualifier(output_qualifiers)
  print("\nChoose output field")
  time.sleep(1)  ### changed from 2 to 1
  output_field_dic=field_choice(fields)
  output_field=output_field_dic["field_name"]
  return input_tuples_list, [output_qualifier,output_field]


def predefined_questions():
  clear_screen()
  
  print("question 1: Provide the address of all homes in British Columbia that are valued over $4,000,000 with a\
  water front view and 4 bedrooms?")
  print('question 2: Which city has the most homes for sale with a 3 car garage and a gas stove?')
  print("question 3: Show me all homes with a master bedroom larger than 120 sq. ft.?")
  print('question 4: Which home has the largest main level size?')
  print('question 5: Provide a list of all realtors in Ontario that work for re/max?')
  print('question 6: Provide a list of all the architects in BC?')
  print('question 7: Provide a list of all the architects in British Columbia.')
  print('question 8: Show me all the homes that have a home theatre room and elevator with a second level area greater than 10 meters squared?')
  print('question 9: Show me all homes that have kitchens suited to chefs?')
  print('question 10: What percentage of homes have a second level larger than the first level?')
  print('question 11: What is the average price per square meter of homes in Alberta?')
  print('question 12: What is the average lot size of homes greater than $3,000,000 in Ontario with a pool and a security system?')
  print('question 13: What appliances are provided in homes valued between $2,000,000 and $3,000,000?')
  selected_question=get_numeric_input('selection [1]: ','1')
  
  if (selected_question=='1'):
    print("[['Province','==','British Columbia'],['Price','>','4000000'],['has','waterfront'],['Bedrooms','==','4']]")
    print("result:")
    print parse_input([['Province','==','British Columbia'],['Price','>','4000000'],['has','waterfront'],['Bedrooms','==','4']])
  elif (selected_question=='2'):
    print "parse_input([['has','gas stove'],['has','garage']])"
    print("result:")
    print parse_input([['has','gas stove'],['has','garage']])
  elif (selected_question=='3'):
    print "parse_input([['Master Bedroom Area','>','11.15']])"
    print("result:")
    print parse_input([['Master Bedroom Area','>','11.15']])
  elif (selected_question=='4'): #'Which home has the largest main level size?'
    max=0
    for key in parse_input([['Main level area','>','0']]):
      if max < float(redis_client.hmget(key,'Main level area')[0]):
        max = float(redis_client.hmget(key,'Main level area')[0])
    print("result:")
    print max,key

  elif (selected_question=='5'): #"Provide a list of all realtors in Ontario that work for re/max?"
    print "parse_input([['Province','==','Ontario']])"
    print("result:")
    print parse_input([['Province','==','Ontario']])

  elif (selected_question=='6'): #'Provide a list of all the architects in BC?'
    print "parse_input([['Province','==','British Columbia'],['has','builder\s|architect\s']])"
    print("result:")
    print parse_input([['Province','==','British Columbia'],['has','builder\s|architect\s']])

  elif (selected_question=='7'): #'Provide a list of all the architects in British Columbia.'
    print "parse_input([['Province','==','British Columbia'],['has','builder\s|architect\s']])"
    print("result:")
    print parse_input([['Province','==','British Columbia'],['has','builder\s|architect\s']])

  elif (selected_question=='8'): #'Show me all the homes that have a home theatre room and elevator with a second level area greater than 10 meters squared?'
    print "parse_input([['has','theatre'],['has','elevator']])"
    print("result:")
    print parse_input([['has','theatre'],['has','elevator']])


  elif (selected_question=='9'): #Show me all homes that have kitchens suited to chefs?'
    print "parse_input([['has','chef']])"
    print("result:")
    print parse_input([['has','chef']])

  elif (selected_question=='10'): #What percentage of homes have a second level larger than the first level?'
    max = 0
    for key in parse_input([['Main level area','>','0']]):
      if max < float(redis_client.hmget(key,'Main level area')[0]):
        max = float(redis_client.hmget(key,'Main level area')[0])
    print("result:")
    print max,key

  elif (selected_question=='11'): #What is the average price per square meter of homes in Alberta?'
    prices = 0
    meters=0
    for key in parse_input([['Province','==','Alberta']]):
      if not redis_client.hmget(key,'final')[0] == None:
        prices +=float(redis_client.hmget(key,'Price')[0])
        meters+=float(redis_client.hmget(key,'final')[0])
    print("result:")
    print 'Average price per SQ Meter:=',prices/meters

  elif (selected_question=='12'): #What is the average lot size of homes greater than $3,000,000 in Ontario with a pool and a security system?'
    print "parse_input([['Price','>','3000000'],['has','pool'],['has','security']])"
    print("result:")
    print parse_input([['Price','>','3000000'],['has','pool'],['has','security']])


  elif (selected_question=='13'): #What appliances are provided in homes valued between $2,000,000 and $3,000,000?'
    print "parse_input([['Price','=>','2000000'],['Price','<=','3000000']])"
    print("result:")
    print parse_input([['Price','=>','2000000'],['Price','<=','3000000']])

  return


fields=[\
#{"field_name":"Document Name", "field_type":"text"},\
{"field_name":"Document Date", "field_type":"date"},\
#{"field_name":"Document Type", "field_type":"text"},\
#{"field_name":"Document Source", "field_type":"text"},\
#{"field_name":"Document Location", "field_type":"text"},\
{"field_name":"Street Address", "field_type":"text"},\
{"field_name":"City", "field_type":"text"},\
{"field_name":"Province", "field_type":"text"},\
{"field_name":"Postal Code", "field_type":"text"},\
{"field_name":"Price", "field_type":"numeric"},\
{"field_name":"Listing id", "field_type":"text"},\
#{"field_name":"Property Type", "field_type":"text"},\
{"field_name":"Building Type", "field_type":"text"},\
{"field_name":"Storeys", "field_type":"numeric", "range_lower":0, "range_upper":1000},\
{"field_name":"Community Name", "field_type":"text"},\
#{"field_name":"Title", "field_type":"text"},\
#{"field_name":"Land Size Length", "field_type":"numeric", "range_lower":0},\
#{"field_name":"Land Size Length Unit", "field_type":"unit", "values":["meters","feet"]},\
#{"field_name":"Land Size Width", "field_type":"numeric", "range_lower":0},\
#{"field_name":"Land Size Width Unit", "field_type":"unit", "values":["meters","feet"]},\
{"field_name":"Parking type", "field_type":"text"},\
{"field_name":"Amenities Nearby", "field_type":"text"},\
{"field_name":"Features", "field_type":"text"},\
{"field_name":"Parking Type", "field_type":"text"},\
{"field_name":"Total Parking Spaces", "field_type":"numeric", "range_lower":0},\
{"field_name":"Basement Features", "field_type":"text"},\
{"field_name":"Basement Type", "field_type":"text"},\
{"field_name":"Bathrooms", "field_type":"numeric", "range_lower":0},\
#{"field_name":"Bedrooms Above Grade", "field_type":"numeric", "range_lower":0},\
#{"field_name":"Bedrooms Below Grade", "field_type":"numeric", "range_lower":0},\
{"field_name":"Bedrooms", "field_type":"numeric", "range_lower":0},\
{"field_name":"Cooling", "field_type":"text"},\
{"field_name":"Exterior Finish", "field_type":"text"},\
{"field_name":"Heating Fuel", "field_type":"text"},\
{"field_name":"Heating Type", "field_type":"text"},\
{"field_name":"Style", "field_type":"text"}]
#{"field_name":"Room Level", "field_type":"text"},\
#{"field_name":"Room Type", "field_type":"text"},\
#{"field_name":"Room Length", "field_type":"numeric", "range_lower":0},\
#{"field_name":"Room Length Unit", "field_type":"unit", "values":["meters","feet"]},\
#{"field_name":"Room Width", "field_type":"numeric", "range_lower":0},\
#{"field_name":"Room Width Unit", "field_type":"unit", "values":["meters","feet"]},\
#{"field_name":"Walk Score", "field_type":"numeric", "range_lower":0,"range_upper":100},\
#{"field_name":"Dependence", "field_type":"text"},\
#{"field_name":"Realtor Names", "field_type":"text"},\
#{"field_name":"Realtor Phone Number", "field_type":"phone"},\
#{"field_name":"Real Estate Company", "field_type":"text"},\
#{"field_name":"Real Estate Address", "field_type":"text"},\
#{"field_name":"Real Estate City", "field_type":"text"},\
#{"field_name":"Real Estate Province", "field_type":"text"},\
#{"field_name":"Real Estate Postal Code", "field_type":"text"},\
#{"field_name":"Real Estate Phone Number", "field_type":"phone"},\
#{"field_name":"Real Estate Fax Number", "field_type":"phone"}]

# required keys: field_name, field_type
# possible field_type values:
# * text
# * date
# * phone
# * unit
# * numeric

# if field_type==unit, then more keys are possible:
# values:["meters","feet"]

# if field_type==number, then more keys are possible:
# * range_lower
# * range_upper

numeric_relation_types=["<", "<=",">",">=","=="] ###mike changed = to ==
numeric_list_operations=["greatest","least","average"]
text_relation_types=["==", "!="]
###output_qualifiers=["set of","percentage of","average value from list","which X has max count","which X has min count"]
output_qualifiers=["set of"]

print("1 choose pre-defined question")
print("2 create new question")
selected_question=get_numeric_input('selection [1]: ','1')
clear_screen()
if (selected_question=='1'):
  predefined_questions() 
  exit()
elif (selected_question=='2'):
  [user_input,user_output]=user_prompt(fields,numeric_relation_types,text_relation_types,output_qualifiers,numeric_list_operations)
#  print("query tuple(s):")
  #print(parse_input(user_input))
 # print("output qualifier and field:")


#result_list=input_tuple_search((user_input[0][1],user_input[0][2],user_input[0][3]))
#print result_list


#print parse_input(user_input)

#result_list=input_tuple_search((user_input[0][1],user_input[0][2],user_input[0][3]))
#print result_list

print(user_output[1])
print parse_input(user_input)

total=0
count=0
max=0
min=10**100000
for property_id in parse_input(user_input):
  try:
    value=float(redis_client.hmget(property_id,user_output[1])[0])
    print value,property_id
    total+=value
    count+=1
    if max < value:
      max = value
      max_key_id=property_id
    if min >value:
      min = value  
      min_key_id=property_id
    
  except:
    print redis_client.hmget(property_id,user_output[1])[0],property_id
#for key in parse_input(user_input):
  
if total !=0:
  print '\n',"Average:=",float(total)/count
  print "Maximum:= ",max,max_key_id
  print "Minimum:= ",min,min_key_id
  
