
# coding: utf-8
import docx
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

provinces=["AB","Alberta","BC","British Columbia",'MB',"Manitoba",'NB',"New Brunswick",'NL',"Newfoundland",'NS',"Nova Scotia",'NT',"Northwest Territories",'NU',\
"Nunavut",'ON',"Ontario",'PE',"Prince Edward Island",'QC',"Quebec",'SK','Saskatchewan','YT','Yukon']

keys=['Property Type','Building Type','Title','Land Size','Built in','Parking Type','Show measurements in','Features',\
'Parking Type','View','Waterfront','Zoning ID','Bathrooms (Total)','Fireplace','Floor Space','Style']

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

for filename in os.listdir(path_to_PDFs):
    if filename[-4:].lower()=='docx':
        data=getText(path_to_PDFs+filename)
        filename=filename[:-5]

        #description and maps general keys
        Description=re.findall('Description(.*)Details',data,re.DOTALL|re.MULTILINE)[0]

        redis_client.hmset(filename,{'Description':Description})

        for indx,line in enumerate(data.split('\n')):
            if re.findall('\-|:',line):
                key_pair=re.split('\-\-:|::|:|\--|\-|;',line)
                redis_client.hmset(filename,{key_pair[0]:key_pair[1]})
            
            elif '$' in line:
                if indx <10:
                    line=re.sub('\$|\,','',line)
               
                    redis_client.hmset(filename,{'Price':float(line)})
            for province in provinces:
                if province in line and indx<10:
                    redis_client.hmset(filename,{'Address':line})
            else:
                for key in keys:
                    if re.findall(key+'$',line):
                        redis_client.hmset(filename,{key:data.split('\n')[indx+1]})


        if re.findall('Rooms(.*)Land?',data,re.DOTALL):
            Rooms=re.findall('Rooms(.*)Land?',data,re.DOTALL)[0]
            Rooms=re.sub('\s\m\s?',' ',Rooms)
            Rooms=re.sub(r"(\d)'(\d)",r'\1*0.3048+0.0254*\2',Rooms)
            Rooms=re.sub(r"(\d)\s?ft\s?",r'\1*0.3048',Rooms)
            Rooms=re.sub(r'(\d)\s*in',r'+\1*0.0254',Rooms)
            Rooms=re.split('\n|([0-9\.\*\+]+\s?[x|X]\s?[0-9\.\*\+]+|\S+\s[Ll]evel)',Rooms)
            Rooms=[x for x in Rooms[3:] if x !=None]
            level=dict()
            d=dict()
            area=0
            total_area=0
            level_name=''
            for indx,line in enumerate(Rooms):

                if re.findall('[lL]evel',line):
                    level[line]=d
                    level_name=line

                elif re.findall('x|X',line):

                    level[level_name+'_area']=total_area
                    match=re.split('x|X',line)
                    match[0]=eval(match[0])
                    match[1]=eval(match[1])
                    area=float(match[0])*float(match[1])
                    
                    Rooms[indx]=[float(match[0]),float(match[1]),area]
                    total_area+=area
                    d[Rooms[indx-1].strip()]=Rooms[indx]

            redis_client.hmset(filename,level)     
