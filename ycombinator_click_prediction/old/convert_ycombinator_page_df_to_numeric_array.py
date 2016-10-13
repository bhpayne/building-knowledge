import pandas as pd
import os.path # file detection
import pickle
import re
import numpy as np
from tqdm import tqdm # (Progress Meter) sudo pip install tqdm # https://pypi.python.org/pypi/tqdm

def max_value_in_dic(this_dic):
    max_value=-1
    for key,value in this_dic:
        if (value>max_value):
            max_value=value
    if (max_value==-1):
        print("error in dic?")
    return max_indx

df = pd.read_pickle('ycombinator.pkl')

if os.path.isfile('data/publishers_list.pkl'):
    publishers_list=pickle.load( open( 'data/publishers_list.pkl', 'rb' ) )
else:
    publishers_list=[]
if os.path.isfile('data/domains_list.pkl'):
    domains_list=pickle.load( open( 'data/domains_list.pkl', 'rb' ) )
else:
    domains_list=[]
if os.path.isfile('data/words_list.pkl'):
    words_list=pickle.load( open( 'data/words_list.pkl', 'rb' ) )
else:
    words_list=[]

f=open('stop_word_list.txt','r')
stop_words=f.read()
stop_words_list= stop_words.split('\n')

list_of_new_publishers=df['publisher'].tolist()
for this_publisher in list_of_new_publishers:
    if this_publisher not in publishers_list:
        publishers_list.append(this_publisher)
pickle.dump( publishers_list, open( "data/publishers_list.pkl", "wb" ) )

list_of_new_domains=df['Domain'].tolist()
for this_domain in list_of_new_domains:
    if this_domain not in domains_list:
        domains_list.append(this_domain)
pickle.dump( domains_list, open( "data/domains_list.pkl", "wb" ) )

list_of_titles=df['Title'].tolist()
list_of_new_words=[]
for this_title in list_of_titles:
    split_title_list=this_title.split(' ')
    for this_word in split_title_list:
        # this would be the place to use regex to remove 's and : and ? ( and )
        this_word=re.sub('\'s|\?|:|\(|\)|\,','',this_word)
        list_of_new_words.append(this_word.lower())
sorted_word_list_dedup=sorted(list(set(list_of_new_words)))
# print(sorted_word_list_dedup)

for this_word in sorted_word_list_dedup:
    if (this_word not in words_list) and (this_word not in stop_words_list):
        words_list.append(this_word)
pickle.dump( words_list, open( "data/words_list.pkl", "wb" ) )


#print(words_list)

# Mike's method to get all of the unique words in a column 
# results=set()  
# df.ix[:,1].str.lower().str.split(' ').apply(results.update) # convert 'Titles' column to lowercase, split on ' '. Apply = to entire column; update = in-place change
# print sorted(results)

df.replace('',np.NaN,regex=True,inplace=True)
df=df.fillna(np.NaN)
# print(df)
# exit()

print(df.shape)
print("add a column per word, per publisher, per domain")
for this_publisher in publishers_list:
    df[this_publisher]=0
for this_domain in domains_list:
    df[this_domain]=0
for this_word in words_list:
    df[this_word]=0

print(df.shape)

# print(df)

# for every word in "words_list" and for every row, is that word contained in the title?
for word in tqdm(words_list):
#     print word
    indx=df[df.Title.str.contains(word)].index
    df[word].ix[indx]=1
# print df[word].ix[indx]
for word in tqdm(domains_list):
    indx=df[df.Title.str.contains(word)].index
    df[word].ix[indx]=1
for word in tqdm(publishers_list):
    indx=df[df.Title.str.contains(word)].index
    df[word].ix[indx]=1

df.drop("Title",inplace=True,axis=1)
df.drop("Domain",inplace=True,axis=1)
df.drop("publisher",inplace=True,axis=1)
df.drop("urls",inplace=True,axis=1)

df['clicked_link']=0
df['clicked_comments']=0
df['clicked_domain']=0
df['clicked_publisher']=0

print(df.shape)
# print(df)

df.to_pickle('numeric_df.pkl')

