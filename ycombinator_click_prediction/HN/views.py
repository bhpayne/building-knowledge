from django.shortcuts import render
import requests,re,io,json
import pandas as pd
from django_user_agents.utils import get_user_agent
from IPython.display import HTML
from datetime import datetime
from HN.models import ycombinator, stories, similar_articles,comments
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import numpy as np
from simserver import SessionServer
import logging
from gensim import utils
from django.db.models import Q
#from .forms import feedbackForm
pd.options.mode.chained_assignment = None 
from django.shortcuts import redirect
def _removeNonAscii(s): return "".join(i for i in s if ord(i)<128) #removes non ascii characters from strings

def get_stories():
    resp=requests.get('https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty').content
    start=int(resp.replace('\n',''))
    for ix in range(start,start-7000,-1):
        data=requests.get('https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(ix)).json()
        try:
            stories(
            time=data['time'],
            comments=str(data['descendants']),
            points=int(data['score']),
            title=_removeNonAscii(data['title']),
            author=str(data['by']),
            url=str(data['url']),
            ID=str(data['id']),
            domain='//'.join(re.split('//|/',data['url'])[:2])
            ).save()
            print 'ix'
        except Exception,e: print str(e)


from time import time
import requests
from HN.models import stories
#filtering=int(time())-604800
def update_comments():
    filtering=int(time())-172800
    lst=[(x[0],x[1]) for x in stories.objects.filter(time__gte=filtering).values_list('ID','pk')]
    for ix in lst:
           data=requests.get('https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(ix[0])).json()
           try:
                   story_obj=stories.objects.get(pk=ix[1])
                   story_obj.comments=data['descendants']
                   story_obj.save()
                   print ix[0],'*'
           except:
                   print 'failed'

def tdelta(strng):#working on a time converter for deltatime 
    resp=re.split('0 days|\.',strng)
    resp=resp[1].strip() if resp[0]=='' else resp[0]
    resp=re.sub('1 days?.*','1 day ago',resp)
    resp=re.sub(r'(\d+) days.*',r'\1 days ago',resp)
    resp=re.split(':',resp)
    resp=resp[0] if resp[0]!='00' else resp[1] +' minutes ago'
    resp=re.sub('1 minutes.*','1 minute ago',resp)
    if 'day' in resp or 'minute' in resp:
         return resp
    else:
         return resp + ' hour ago' if resp=='1' else resp + ' hours ago'

def drop_after2(df,col,sortby):
    df=df.sort_values(sortby,ascending=False)
    keep1=df[col].drop_duplicates().index.tolist()
    keep2=df.drop(keep1)[col].drop_duplicates().index.tolist()
    return pd.concat([df.ix[keep1],df.ix[keep2]])


def db_write(request,item=None,item2=None):
    data=stories.objects.filter(ID=item2).values()[0]
    ycombinator(
        url_clicked_on=data[item],
        user_agent=request.META["HTTP_USER_AGENT"] or None,
        ip_address=request.META["HTTP_X_FORWARDED_FOR"] or None,
        time_stamp=data['time'],
        parsed_user_agent=get_user_agent(request),
        comments=data['comments'],
        points=data['points'],
        title=data['title'],
        domains=data['domain'],
        author=data['author'],
        time=datetime.now(),
        article=data['ID'],
        ).save()
    return HttpResponseRedirect('https://sheltered-temple-21142.herokuapp.com')


def get_new_content(request):
    stories_list=get_stories_list()
    for ix in stories_list[:50]:
        data=requests.get('https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(ix)).json()
        try:
            stories(
            time=data['time'],
            comments=str(data['descendants']),
            points=int(data['score']),
            title=_removeNonAscii(data['title']),
            author=str(data['by']),
            url=str(data['url']),
            ID=str(data['id']),
            domain='//'.join(re.split('//|/',data['url'])[:2])
            ).save()
            print 'ix'
        except:
            print ''
    return HttpResponseRedirect('https://sheltered-temple-21142.herokuapp.com')
from time import time


def db_index(request,id=None):
    filtering=int(time())-604800
    lst=[pd.Series(x) for x in stories.objects.filter(time__gte=filtering).values()]
    df=pd.concat(lst,axis=1).T
    df['domain']=df.url
    df['time_stamp']=df.time
    df=df[['comments','time','points','title','author','url','ID','domain','time_stamp']]
    df.time=df.time.apply(lambda x: datetime.now()-datetime.fromtimestamp(float(x)) or '')
    df=df.sort_values('time')
    df=df.ix[:100]
    col=df.columns
    user_agent=request.META["HTTP_USER_AGENT"]
    context={'instance':df.iterrows(),'user_agent':user_agent,'col':col}
    return render(request,'index.html',context)

def history(request):
    lst=[pd.Series(x) for x in ycombinator.objects.filter(user_agent=request.META["HTTP_USER_AGENT"]).values()]
    #lst=[pd.Series(x) for x in ycombinator.objects.all().values()]
    if len(lst)==0:
        return render(request,'index.html')
    else:
        df=pd.concat(lst,axis=1).T
        
        df=df[['comments','time','points','title','author']]
        
        user_agent=request.META["HTTP_USER_AGENT"]
        
        col=df.columns
        context={
        'lst':lst,
        'df':df.iterrows(),
        'user_agent':user_agent,
        'instance':df.iterrows(),
        'col':col,
        }
        
    
        return render(request,'history.html',context)




def suggested(request):
    lst=[pd.Series(x) for x in ycombinator.objects.filter(user_agent=request.META["HTTP_USER_AGENT"]).values()]
    df=pd.concat(lst,axis=1).T
    df=df[['title']]
    texts = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]
    corpus = [{'id': 'doc_%i' % num, 'tokens': utils.simple_preprocess(text)}
              for num, text in enumerate(texts)]    
    service = SessionServer('static/')
    service.train(corpus, method='lsi')
    service.index(corpus)
    #data=service.find_similar('doc_0')
    data=df
    context={
    #'data':data.iterrows(),
    'data':data.title
    }
    return render(request,'suggested.html',context)

from HN.models import similar_articles

def similar(request):
    lst=[pd.Series(x) for x in ycombinator.objects.filter(user_agent=request.META["HTTP_USER_AGENT"]).values()]
    df=pd.concat(lst,axis=1).T
    data=df.article.tolist()
    data2=[x[1:] for x in similar_articles.objects.filter(Q(article1__in=data) | Q(article2__in=data)).values_list()]

    lst2=[pd.Series(x) for x in stories.objects.all().values()]
    tf=pd.concat(lst2,axis=1).T
    f=lambda x:tf.title[tf.ID==x].tolist()[0]
    data2=[(x[0],f(str(x[0])),x[1],f(str(x[1])),x[2]) if x[0] in data else (x[1],f(str(x[1])),x[0],f(str(x[0])),x[2]) for x in data2 ]
    tf=pd.DataFrame(data2,columns=['a','b','c','d','e'])
    tf=drop_after2(tf,'a','e')
    data2=tf.drop_duplicates(['a','c'])
    #data2=zip(data2,data)
    context={'data':data,'data2':data2.iterrows()}
    return render(request,'suggested.html',context)



def sim():
    service = SessionServer('HN/static/')
    lst=[pd.Series(x) for x in stories.objects.all().values()]
    df=pd.concat(lst,axis=1).T
    df['domain']=df.url
    df['time_stamp']=df.time
    df=df[['comments','points','title','author','url','ID','domain']]
    #df.time=df.time.apply(lambda x: str((datetime.now()-datetime.fromtimestamp(float(x)))).rsplit(':',1)[0] or '')
    #df=pd.concat(pd.read_html('https://sheltered-temple-21142.herokuapp.com'))
    df=df.applymap(lambda x:str(x))
    df.title=df.title.apply(lambda x:_removeNonAscii(x))
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
            if item[1]>.4:
                lst.append((ix['id'],item[0],item[1]) if ix['id']!=item[0] else '')

    lst=[x for x in lst if x!='']
    f=open('HN/static/similar.txt','w')
    f.write(str(sorted(lst,key=lambda x: -x[2])))
    print lst

def about(request):
    return render(request,'about.html')






from .forms import testForm

def feedback(request):
    if request.method == "POST":
        form = testForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            comments(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                feedback=request.POST.get('feedback')

                ).save()
            #post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect('https://sheltered-temple-21142.herokuapp.com')
    else:
        form = testForm()
    return render(request, 'feedback.html', {'form': form})
from .forms import morelessForm
def delkeep(request):
    if request.method == "POST":
        form = morelessForm(request.POST)
    else:
        form = morelessForm()
    return render(request, 'delkeep.html', {'form': form})
    

import os
from neo4j.v1 import GraphDatabase, basic_auth

