# from Mike
# 20151219

import requests
import re
import pandas as pd
#from selenium import webdriver  
#from selenium.webdriver.common.keys import Keys
import numpy as np
pd.options.mode.chained_assignment = None 
#import sys
#reload(sys)  
#sys.setdefaultencoding('utf8') # enables export to CSV of unicode
pd.set_option('display.max_rows', 1000)
pd.set_option('max_colwidth',700)
pd.set_option('display.width', 1000)
tf=pd.DataFrame()
def f(x):
    return x[0] not in x[1]


def get_page(page,tf=tf):
    url='https://news.ycombinator.com/news?p={}'.format(page)
    data=requests.get(url).content           #grabs the html
    df=pd.read_html(data)[2].fillna('')      #grabs the correct table from the html
    df=df[[0,2,1]]                           #sort colums
    df[1]=df[1].shift(-1)                    #align data
    df.columns=['number','Title','Points'] #rename columns
    lst=df.Points.str.replace('points by|ago|\||comments?|discuss',' ').str.split('\s+').tolist()[0::2] #clean content
    df=df.ix[0::2] #remove empty rows
    df.drop('Points',1,inplace=True) #removed column
    df=df.reset_index(drop=True) #reset indicies
    df=pd.concat([df,pd.DataFrame(lst[:-1])],axis=1) #merged dataframes
    df=df.ix[:,:-1] #dropping a column
    df.columns=['number','Title','points','publisher','time','hours','comments'] #adding names to columns
    df.drop('hours',1,inplace=True) #droped columns
    df.replace('None','',inplace=True) #replace Nones
    domains=pd.DataFrame(df.Title.str.split('(',).tolist()) #extracting the domains
    domains=domains.ix[:,1:] #
    domains.ix[:,1][domains.ix[:,2].str.len()>0]=domains.ix[:,2] #
    domains=domains.ix[:,1] #
    df['Domain']=domains.replace('\)','',regex=True) #
    df=df[df.Domain.notnull()]   
    try:
        df['urls']=re.findall('href="(http.{,150})',data)[1:-2]  #finds the complete urls
    except:
                                    #drop rows where domain is null
        print 'length of the dataframe',len(df)                 #testing for mismatch of length of urls and lenght of df
        print 'length of urls',len(re.findall('href="(http.{,150})',data)[1:-1])
        df['urls']=re.findall('href="(http.{,150})',data)[1:-1]
        df['comments_url']=re.findall('(item\?id.*?)"',data)[0::2]
        
        df['comments_url']='https://news.ycombinator.com/'+df['comments_url']
    df.urls.replace('".*','',regex=True,inplace=True)  #clean urls
    df.Title=df.Title.replace(df.Domain,'',regex=True) #cleaning Title
    df.Title=df.Title.replace('\(\)','',regex=True)# cleaning Title column
    df.comments=df.comments.replace('None','',regex=True) # convert to float issue
    df.points=df.points.apply(float) #convert nums to float
    df=df.sort_values('points',ascending=False) #sort by points, comments needs work before you can sort by comments pts
    return df


for page in xrange(1,2):   #set the number of pages that you want to grab limit is around 38 more than that and they return a blank page
    try:
        tf=pd.concat([tf,get_page(page)])
    except:
      
        pass
    

#df.to_excel('ycombinator.xls') #write to excel
#tf.to_csv('ycombinator.csv') #write to CSV
results=set()  #gets all of the unique words in a column 

print(results)

tf.ix[:,1].str.lower().str.split(' ').apply(results.update) #
tf.reset_index(drop=True,inplace=True)
tf.urls[tf[['Domain','urls']].apply(f,axis=1)]='' #removes url in the case that the domain and url do not match /better solution needed
tf.to_pickle('ycombinator.pkl')

# f=open('word_list.txt','w')
# f.write(str(sorted(results))
