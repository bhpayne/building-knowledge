from simserver import SessionServer
import logging
from gensim import utils
from HN.models import *
from HN.views import sim
from HN.models import stories
from HN.models import ycombinator
import pandas as pd
from HN.models import similar_articles
from HN.models import similar_articles as sa

def _removeNonAscii(s): return "".join(i for i in s if ord(i)<128)
service = SessionServer('HN/static/')
import logging
lst=[pd.Series(x) for x in stories.objects.all().values()]
df=pd.concat(lst,axis=1).T
df['domain']=df.url
df['time_stamp']=df.time
df=df[['comments','points','title','author','url','ID','domain']]
df=df.applymap(lambda x:str(x))
df.title=df.title.apply(lambda x:_removeNonAscii(x))
df.title=df.title.str.replace('[pdf]','')
lst=[]
for ix in df.iterrows():
    lst.append(' '.join(list(ix[1])))

texts=lst
corpus = [{'id': 'doc_%i' % num, 'tokens': utils.simple_preprocess(text)}
           for num, text in enumerate(texts)]
service.train(corpus, method='lsi')
service.index(corpus)
lst=[]
for ix in corpus:
    score=service.find_similar(ix['id'])
    for item in score:
        if item[1]>.7:
            lst.append((ix['id'],item[0],item[1]) if ix['id']!=item[0] else '')



lst=[x for x in lst if x!='']
lst=[(int(x[0].split('_')[1]),int(x[1].split('_')[1]),x[2]) for x in lst]
results=[(df.ID.ix[x[0]],df.ID.ix[x[1]],x[2]) for x in lst]
sorted(results,key=lambda x: -x[2])
results=sorted(results,key=lambda x: -x[2])
sa.objects.all().delete()
[sa(article1=x[0],article2=x[1],score=x[2]).save() for x in results]


