import requests
import re
import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None 
pd.set_option('display.max_rows', 1000)
pd.set_option('max_colwidth',700)
pd.set_option('display.width', 1000)
tf=pd.DataFrame()

##################### date urls
date_url='https://web.archive.org/web/*/https://news.ycombinator.com'
data=re.findall('/web/.{30,70}',requests.get(date_url).text) #request
date_urls=pd.DataFrame(data).replace('".*','',regex=True)[7:] #clean
date_urls.reset_index(drop=True,inplace=True) #reset index
date_urls='https://web.archive.org'+date_urls #all of the dates from wayback

html=requests.get(date_urls.ix[7000].tolist()[0]).content    
df=pd.read_html(html)[3].ix[:,:2] #read in dataframe
df[1]=df[1].shift(-1) #align data
df=df.dropna(how='all')[4:-2].reset_index(drop=True) #clean dataframe
df.columns=['Number','Points','Title'] #name columns 

df.Points=df.Points.replace('points by|hours?|days?|ago|\||comments?','',regex=True)
points_df=pd.DataFrame(df.Points.str.split('\s+').tolist()).ix[:,:3]
df=pd.concat([df,points_df],axis=1)#combine points dataframe and df
df.drop('Points',axis=1,inplace=True)#drop points column

domains=pd.DataFrame(df.Title.str.split('(',).tolist())     #extracting the domain
domains.ix[:,1][domains.ix[:,2].str.len()>0]=domains.ix[:,2] #
domains=domains.ix[:,1] #
df['Domain']=domains.replace('\)','',regex=True) #

df.Title=df.Title.replace(df.Domain,'',regex=True) #cleaning Title
df.Title=df.Title.replace('\(\)','',regex=True)# cleaning Title column


urls=re.findall('http.{,100}',html)
urls_df=pd.DataFrame(urls).replace('https?://.{3,}.ycombinator.com.*|http://faq.web.archive.org.*','',regex=True)
urls_df=urls_df.replace('https://github.com/HackerNews/AP.*|https://hn.algolia.com/.*','',regex=True)
urls_df=urls_df[urls_df[0]!='']
urls_df.reset_index(drop=True,inplace=True)
urls_df.replace('".*','',regex=True,inplace=True)


df=pd.concat([df,urls_df],axis=1)
df.column=['Number','Title','Points','Author','Time','Comments','Domain','Urls']

