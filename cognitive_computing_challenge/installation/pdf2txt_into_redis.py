import os
import re
from redis import Redis
import yaml # used to read "config.input"

# connect to local Redis DB
redis_client=Redis(host='127.0.0.1', port=6379, db = 0)

# https://yaml-online-parser.appspot.com/
input_stream=file('config.input','r')
input_data=yaml.load(input_stream)
path_to_PDFs=input_data["path_to_PDFs"]

path_to_dirs=path_to_PDFs+'content_extracted_from_documents/'
list_of_dir=os.listdir(path_to_dirs)
#finds all of the keys for the dictionary in the pdf... Needs a little work 

def find_keys(data):
    dict_keys = []
    test_keys = re.findall('^[A-Z]{1,}[a-z]+.*',str(data),re.MULTILINE)
    for item in test_keys:
        if test_keys.count(item)%4==0 and item not in dict_keys:
            dict_keys.append(item)
    return dict_keys   


provinces=["AB","Alberta","BC","British Columbia",'MB',"Manitoba",'NB',"New Brunswick",'NL',"Newfoundland",'NS'\
           "Nova Scotia",'NT',"Northwest Territories",'NU'\
           "Nunavut",'ON',"Ontario",'PE',"Prince Edward Island",'QC',"Quebec",'SK','Saskatchewan','YT','Yukon'] 
def map_keys(data):
    keywords = dict()
   
    keywords['Document Name']=filename[:-4]
    keywords['Price']= re.findall('^\$\d+,\d+,\d*,*\d*',str(data),re.MULTILINE)[0]
    keywords['Price']=float(keywords['Price'].replace('$','').replace(',',''))
    keywords['Listing id']=re.findall('Listing ID:(\S+)',str(data),re.MULTILINE)[0].strip()
    keywords['Document Date']= re.findall('\d{1,2}/\d{1,2}/\d{2,4}',str(data),re.MULTILINE)[0]
    keywords['Document Source']=re.findall('http:\S+',str(data),re.MULTILINE)[0]
    
    
    keywords['Street Address']= re.findall('\d*\s*\w*\s*\w*\s*\w*,\s*\w*\s*\w*,\s*\w+\s*\w+\s*[A-Z0-9]+',str(data),re.MULTILINE)[0]
    keywords['City']=re.findall('\d*\s*\w*\s*\w*\s*\w*\s*\w*,(\s*\w*\s*\w*),\s*\w+\s*\w+\s*[A-Z0-9]+',str(data),re.MULTILINE)[0]
    keywords['Province']=re.findall('\d*\s*\w*\s*\w*\s*\w*\s*\w*,\s*\w*\s*\w*,(\s*\w+\s*\w+\s*)[A-Z0-9]+',str(data),re.MULTILINE)[0]
    keywords['Postal Code']=re.findall('\d*\s*\w*\s*\w*\s*\w*\s*\w*,\s*\w*\s*\w*,\s*\w+\s*\w+\s*([A-Z0-9]+)',str(data),re.MULTILINE)[0]
    
    #############Address of the property ####################
    data=re.sub('\\x0c','',str(data))
    match =[re.findall('.*'+x+'.*\|',str(data)) for x in provinces if re.findall(x,str(data))  ]
    match_refined=[x for x in match for y in range(len(match)) if len(x)>0]
    try:
        match_refined[0][0]=re.sub('\-?\s?\w+\s?\|','',match_refined[0][0])
        match_refined[0][0]=re.split('\s\s+|\,',match_refined[0][0])
        keywords['Street Address'],keywords['City'],keywords['Province'],keywords['Postal Code']=match_refined[0][0]
        
    except:
        pass
                     
    ##################################################################
    
    
    for i in find_keys(data):
        #data=re.sub('\xc2\xa0','',data)
        #print i,data.split('\n').index(i) 
        if len(data.split('\n')[data.split('\n').index(i) +4])>0:
            keywords[i]=data.split('\n')[data.split('\n').index(i) +4]
            keywords[i]=keywords[i].strip()
        
        #print len(keywords[i].strip())
     
        
        try:
            if float(keywords[i]) and '.' in keywords[i]:
                
                keywords[i]=float(keywords[i])
            elif float(keywords[i]) and '.' not in keywords[i]:
                
                keywords[i]=int(keywords[i])
                  

        except:
            pass
    
    return keywords



for this_dir in list_of_dir:
    filename=path_to_dirs+this_dir+"/pdf2txt.txt"
    
    f=open(filename,"r")
   
    data=f.read()

    redis_client.hmset(this_dir,map_keys(data))
    
  