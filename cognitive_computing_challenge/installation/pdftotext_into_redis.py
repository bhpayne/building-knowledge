import os
import re
from redis import Redis
import yaml # used to read "config.input"

# connect to local Redis DB
redis_client=Redis(host='127.0.0.1', port=6379, db = 0)
redis_client1=Redis(host='127.0.0.1', port=6379, db = 1)
# https://yaml-online-parser.appspot.com/
input_stream=file('config.input','r')
input_data=yaml.load(input_stream)
path_to_PDFs=input_data["path_to_PDFs"]

path_to_dirs=path_to_PDFs+'content_extracted_from_documents/'
list_of_dir=os.listdir(path_to_dirs)
#finds all of the keys for the dictionary in the pdf... Needs a little work 
keywords=dict()
def searching(word,lines_before,lines_after,data):
    lst=[]
    data=re.split('\n',data.lower())
    for indx,line in enumerate(data):
        if word in line.strip():
            data=data[indx-int(lines_before):indx+int(lines_after)]
            for line in data:
                lst.append(line.strip())
    return lst

def flatten(lst):
    return sum( ([x] if not isinstance(x, list) else flatten(x)
             for x in lst), [] )


#########################################################Realtor 

provinces=["AB","Alberta","BC","British Columbia",'MB',"Manitoba",'NB',"New Brunswick",'NL',"Newfoundland",'NS'\
           "Nova Scotia",'NT',"Northwest Territories",'NU'\
           "Nunavut",'ON',"Ontario",'PE',"Prince Edward Island",'QC',"Quebec",'SK','Saskatchewan','YT','Yukon']     

def realtor_parser(data):
    people=[]
    phones=[]
    faxes=[]
    associations=[]
    streets=[]
    titles=[]
    companies=[]
    box_apt_suites=[]
    prov=[]
    
   
        
    
    data=searching('Fax:',8,7,data)
    realtor=dict()
    for indx,line in enumerate(data):
        line =re.sub('Walk.*|Car.*|Data.*|All infor.*','',line)
        if len(line)>0:
            d[indx]=re.split('\s\s+',line)
                
        try:
               
            
            for lst in d.items():
                for items in lst[1:]:
                    for elements in items:
                        
                       match=re.findall('Fax:\s*(\d{3}-\d{3}-\d{4})',elements)
                       if match:
                        faxes.append(match)
                       
                       match=re.findall("^[#\d\-\s]+[A-z]+\s*[A-z]*",elements.strip())
                       if match:
                        streets.append(match)
                       
                       
                       match=re.findall("(sales.*|associate|Broker)",elements,re.IGNORECASE)
                       if match:
                        
                        titles.append(match)
                       
                        
                       match=re.findall('^\d{3}-\d{3}-\d{4}',elements)
                       if match:
                        phones.append(match)
                        
                    
                       
                       match=re.findall('^[A-z]+\s[A-z]+\s*[A-z]*$',elements)
                       if match and elements not in associations and elements not in titles:
                        people.append(match)
                        
                        
                       match=re.findall('.*(?:Select|Properties|Royal|Real|INC.|&|Realty).*',elements,re.IGNORECASE)
                       if match:
                        associations.append(match)
                       
                       
                       match =[elements for x in provinces if x in elements  ]
                       if len(match)>0:
                        prov=match
                    
                       
        except:
            pass
        realtor=dict()
        
        realtor['associations']=flatten(associations)
        
        realtor['Realtor Phone Number']=flatten(phones)
        phones=[]
             

        realtor['titles']=flatten(titles)
        
       
        realtor['Real Estate Fax Number']=flatten(faxes)
        
        realtor['streets']=flatten(streets)
        
        realtor['Real Estate Province']=prov
        realtor['Realtor Names']=[person for person in flatten(people) if person not in flatten(associations) and person not in flatten(titles)]
        people=[]
        associations=[]
        titles=[]
        faxes=[]
        streets=[]
    return realtor    
            


#############################################################################
def room_parser(doc_path):
    lst=[]
    key='NA'
    d=dict()
    for word in searching('Dimensions',0,28,doc_path):
        
        word=re.sub('Walk Score.*|http.*','',word)
        word=re.sub('\sm\s*|\,','',word)
        word=re.sub(r'(\d)\s*in',r'+\1*0.0254',word)
        word=re.sub(r'(\d)\s*(ft|\')\s*',r'\1*0.3048',word)
        
        word=re.split('x|X|\s\s+',word.strip())
        #print word
     
        if len(word)>1 and 'dimensions' not in word[-1].lower():
            if 'level' in word[0].lower() or 'flat'  in word[0].lower(): #or 'other' in word[0].lower():
                #print word[0]
                d[key]=lst
                lst=[]
                key = word[0]
                if not re.findall('[A-z]+',word[-1]) and not re.findall('[A-z]+',word[-2]):
                    word[-1]=eval(word[-1])
                    word[-2]=eval(word[-2])
                
                
                    word.append(float(word[-1])*float(word[-2]))
                lst.append(word[1:])
            
                #if re.findall('[mM]aster bedroom',word[1]):
                  #  print 'master'
                #lst.append(float(word[-1])*float(word[-2]))
                #print lst
            else:
                try:
                    if not re.findall('[A-z]+',word[-1]) and not re.findall('[A-z]+',word[-2]):
                        word[-1]=eval(word[-1])
                        word[-2]=eval(word[-2])
                    
                    
                        word.append(float(word[-1])*float(word[-2]))
                except:
                    pass
                lst.append(word[0:])
                
                d[key]=lst
                #print lst
    try:
        del d['NA']
    except:
        pass
    return d






#####################################################################################


#adds realtor to redis 
d=dict()
for this_dir in list_of_dir:
    filename=path_to_dirs+this_dir+"/pdftotext.txt"
    f=open(filename,"r")
    data=f.read()
    if len(realtor_parser(data))>0:
        redis_client.hmset(this_dir,realtor_parser(data))
    




#adds bedrooms and bathrooms to redis
for this_dir in list_of_dir:
    filename=path_to_dirs+this_dir+"/pdftotext.txt"
    f=open(filename,"r")
    data=f.read()
   

    try:
        beds = eval(re.split('\s\s+',re.findall('\$.*',data)[0])[-2])
  
        baths = eval(re.split('\s\s+',re.findall('\$.*',data)[0])[-1])

        description=re.findall('Description.*',data,re.DOTALL)[0]
        description=re.split('\n\n+',description)[0]
        
        d={'Bedrooms':beds,'Bathrooms':baths,'Description':description}
        
        redis_client.hmset(this_dir,d)
        
    except:
        pass
#sums up areas 
total=0

for this_dir in list_of_dir:
    filename=path_to_dirs+this_dir+"/pdftotext.txt"
    f=open(filename,"r")
    data=f.read()
    
    d=room_parser(data)
    redis_client1.set(this_dir,data)
    
    for keys in d.keys():
        d[str(keys)+ ' area']=0
        for lst in d[keys]:
            try:
                match=re.findall('[mM]aster bedroom',lst[0])
                if match:
                    d['Master Bedroom Area']=lst[-1]
                    
                d[str(keys)+ ' area']+=float(lst[-1])
             
                total+=float(lst[-1])
          
            except:
                pass
   
        #print d
    if len(d) > 0:
            #print file
            d['final']=total
            redis_client.hmset(this_dir,d)

