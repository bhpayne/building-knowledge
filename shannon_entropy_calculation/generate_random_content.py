# https://security.stackexchange.com/questions/96370/a-simple-question-about-entropy-and-random-data

import loremipsum
import random
import shannon_entropy_calculation as shan_ent
import math

# this_list=['a','b','a']

# this_list=[]
# for indx in range(1000000):
#   this_list.append(str(random.randint(0,9)))

# this_list=[]
# for indx in range(100000):
#   this_list.append('a')
#   this_list.append('b')

# this_list=[]
# for indx in range(100):
#   [sentences_count, words_count, paragraph]=loremipsum.generate_paragraph()
#   this_list=this_list+list(paragraph)

imp='abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab'
this_list=list(imp)

entropy=shan_ent.calculate_entropy(this_list)
  
print("\nShannon entropy = "+str(entropy))
# print("\nmetric entropy  = "+str(entropy/math.log(len(this_list),2))+"\n")
print("\nmetric entropy  = "+str(entropy/(len(this_list)*1.0))+"\n")
