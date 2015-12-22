import pandas as pd
import os.path # file detection
import pickle

df = pd.read_pickle('ycombinator.pkl')

if os.path.isfile('data/publishers_dic.pkl'):
    publishers_dic=pickle.load( open( 'data/publishers_dic.pkl', 'rb' ) )
else:
    publishers_dic={}
if os.path.isfile('data/domains_dic.pkl'):
    domains_dic=pickle.load( open( 'data/domains_dic.pkl', 'rb' ) )
else:
    domains_dic={}
if os.path.isfile('data/words_dic.pkl'):
    words_dic=pickle.load( open( 'data/words_dic.pkl', 'rb' ) )
else:
    words_dic={}

df['clicked link']=0
df['clicked comments']=0
df['clicked domain']=0
df['clicked publisher']=0

list_of_publishers=df['publisher'].tolist()
indx=0
for this_publisher in list_of_publishers:
    if this_publisher not in publishers_dic:
        publishers_dic[this_publisher]=indx
        indx+=1

# add a new column to the dataframe, "publisher ID". The publisher ID correlates to the publisher via the publisher_dic

# http://stackoverflow.com/questions/26886653/pandas-create-new-column-based-on-values-from-other-columns
# http://stackoverflow.com/questions/18472634/how-to-compute-a-new-column-based-on-the-values-of-other-columns-in-pandas-pyt
# http://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe
# http://stackoverflow.com/questions/10729210/iterating-row-by-row-through-a-pandas-dataframe

for index, row in df.iterrows():
    if row['publisher']

list_of_domains=df['Domain'].tolist()
indx=0
for this_domain in list_of_domains:
    if this_domain not in domains_dic:
        domains_dic[this_domain]=indx
        indx+=1

# Ben's method of creating a dictionary -- each word as key gets unique integer value
list_of_titles=df['Title'].tolist()
indx=0
for this_title in list_of_titles:
    split_title_list=this_title.split(' ')
    for this_word in split_title_list:
        if this_word not in words_dic:
            words_dic[this_word]=indx
            indx+=1

# Mike's method to get all of the unique words in a column 
results=set()  
df.ix[:,1].str.lower().str.split(' ').apply(results.update) # convert 'Titles' column to lowercase, split on ' '
print sorted(results)

# to do: remove stop words

