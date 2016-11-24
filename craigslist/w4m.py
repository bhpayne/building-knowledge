import re
import requests
data=requests.get('http://baltimore.craigslist.org/search/w4m')

def func(ix):
    lst=re.findall('href.*?age.{12}',data.text,re.DOTALL)
    resp=re.sub(
'href=|data-id.{12}|=|class|result-title|hdrlnk|span|result-age|"|</a?>?|<|>',
'',lst[ix]).split(' ')
    return  [x for x in resp if x!='']


dct={}
for ix in range(200):
    try:
        if int(str(func(ix)[-1])) < 36: #age goes here 
            line=' '.join(func(ix))
            if len(re.findall('bbw|smoke',line,re.IGNORECASE))==0:#undesired features
               dct[ix]=line.split(' ') 
    except:
        pass
    
for item in sorted(dct.values(),key=lambda x:x[-1]):#sort by age
    print 'http://baltimore.craigslist.org'+' '.join(item)
