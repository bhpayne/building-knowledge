import pandas as pd
import os.path # file detection
import pickle

def max_value_in_dic(this_dic):
    max_value=-1
    for key,value in this_dic:
        if (value>max_value):
            max_value=value
    if (max_value==-1):
        print("error in dic?")
    return max_indx

df = pd.read_pickle('ycombinator.pkl')

if os.path.isfile('data/publishers_dic.pkl'):
    publishers_dic=pickle.load( open( 'data/publishers_dic.pkl', 'rb' ) )
    max_publisher_indx=max_value_in_dic(publishers_dic)
else:
    publishers_dic={}
    max_publisher_indx=0
if os.path.isfile('data/domains_dic.pkl'):
    domains_dic=pickle.load( open( 'data/domains_dic.pkl', 'rb' ) )
    max_domain_indx=max_value_in_dic(domains_dic)
else:
    domains_dic={}
    max_domain_indx=0
if os.path.isfile('data/words_dic.pkl'):
    words_dic=pickle.load( open( 'data/words_dic.pkl', 'rb' ) )
    max_word_indx=max_value_in_dic(words_dic)
else:
    words_dic={}
    max_word_indx=0

f=open('stop_word_list.txt','r')
stop_words=f.read()
stop_words_list= stop_words.split('\n')

df['clicked_link']=0
df['clicked_comments']=0
df['clicked_domain']=0
df['clicked_publisher']=0

list_of_publishers=df['publisher'].tolist()
indx=max_publisher_indx
for this_publisher in list_of_publishers:
    if this_publisher not in publishers_dic:
        indx+=1
        publishers_dic[this_publisher]=indx

# add a new column to the dataframe, "publisher ID". The publisher ID correlates to the publisher via the publisher_dic

# http://stackoverflow.com/questions/26886653/pandas-create-new-column-based-on-values-from-other-columns
# http://stackoverflow.com/questions/18472634/how-to-compute-a-new-column-based-on-the-values-of-other-columns-in-pandas-pyt
# http://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe
# http://stackoverflow.com/questions/10729210/iterating-row-by-row-through-a-pandas-dataframe

# for index, row in df.iterrows():
#     if row['publisher']

list_of_domains=df['Domain'].tolist()
indx=max_domain_indx
for this_domain in list_of_domains:
    if this_domain not in domains_dic:
        indx+=1
        domains_dic[this_domain]=indx

# Ben's method of creating a dictionary -- each word as key gets unique integer value
list_of_titles=df['Title'].tolist()
list_of_words=[]
for this_title in list_of_titles:
    split_title_list=this_title.split(' ')
    for this_word in split_title_list:
        # this would be the place to use regex to remove 's and : and ?
        list_of_words.append(this_word.lower())
sorted_word_list_dedup=sorted(list(set(list_of_words)))
# print(sorted_word_list_dedup)

indx=max_word_indx
for this_word in sorted_word_list_dedup:
    if (this_word not in words_dic) and (this_word not in stop_words_list):
        indx+=1
        words_dic[this_word]=indx

print(words_dic)

# Mike's method to get all of the unique words in a column 
# results=set()  
# df.ix[:,1].str.lower().str.split(' ').apply(results.update) # convert 'Titles' column to lowercase, split on ' '. Apply = to entire column; update = in-place change
# print sorted(results)

