from django.shortcuts import render
import requests,re,io,json
import pandas as pd
from django_user_agents.utils import get_user_agent
from IPython.display import HTML
from datetime import datetime
from HN.models import ycombinator, stories, similar_articles
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import numpy as np
from simserver import SessionServer
import logging
from gensim import utils
from django.db.models import Q
pd.options.mode.chained_assignment = None 
def _removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

lst=[str(x) for x in range(11604691-25000,11604691-32000,-1)]
new_list=[]
def get_content(lst):
    for ix in lst:
        try:
            data=requests.get('https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(ix)).json()
            if 'descendants' in data.keys():
                new_list.append(data)
        except:
            print ''
            

def get_new_content(data):
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

get_content(lst)
for ix in new_list:
    data=ix
    try:
        get_new_content(data)
        print '*'
    except:
        print ''