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
    for ix in range(start,start-2000,-1):
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


get_stories()
update_comments()
import retrain