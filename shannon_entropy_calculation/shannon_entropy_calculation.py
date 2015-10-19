# reproducing http://www.shannonentropy.netmark.pl/
# http://www.lptmc.jussieu.fr/user/lesne/MSCS-entropy.pdf
# http://arxiv.org/abs/1405.2061

# http://blog.dkbza.org/2007/05/scanning-data-for-entropy-anomalies.html
# http://stackoverflow.com/questions/990477/how-to-calculate-the-entropy-of-a-file

import math

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
      print("\n--> no selection from user; defaulting to ")
      number_provided=True
      input_number=default_choice
    try:
      print(int(input_number))
      number_provided=True
    except ValueError:
      print("\n--> invalid choice - not an integer; try again")
  return input_number

def get_input_string():
  user_input_list=[]
  print("1    provide single-line string")
  print("2    provide file name")
  print("0    exit")
  user_choice=get_numeric_input("selection [0]: ","0")

  valid_input=False
  while(not valid_input):
    if (int(user_choice)==0):
      valid_input=True
      exit()
    elif (int(user_choice)==1):
      valid_input=True
      user_string=get_text_input('provide input: ')
      user_input_list=list(user_string)
#       print(user_input_list)
    elif (int(user_choice)==2):
      valid_input=True
      user_string=get_text_input('file name: ')
      with open (user_string, "r") as myfile:
        data=myfile.read()
      user_input_list=list(data)  
    else:
      print("invalid input; try again")
      valid_input=False

  return user_input_list

def calculate_entropy(user_input_list):
  entropy=0.0
  for this_char in list(set(user_input_list)):
    number_of_times_this_char_appears=user_input_list.count(this_char)
    probability_of_this_char=number_of_times_this_char_appears/(len(user_input_list)*1.0)
    print(this_char+" : count="+str(number_of_times_this_char_appears)+", prob="+str(probability_of_this_char))

# H(x) = -\sum_{i=1}^n p(x_i) \log_b p(x_i)  
    entropy -= probability_of_this_char * math.log(probability_of_this_char,2)
  return entropy

# user_input_list=get_input_string()
# print(user_input_list)
# 
# entropy=calculate_entropy(user_input_list)
#   
# print("\nShannon entropy = "+str(entropy))
# print("\nmetric entropy  = "+str(entropy/math.log(len(user_input_list),2))+"   where 1 means equally distributed random string\n")
# print("\nmetric entropy  = "+str(entropy/(len(user_input_list)*1.0))+"   where 1 means equally distributed random string\n")


