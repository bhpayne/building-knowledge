from django.conf.urls import include, url
from django.contrib import admin
from HN import views as HN_Views
urlpatterns = [
    ##url(r'^$|Comments|Points|Author|Time|Title|Domain',HN_Views.db_sort),
    url(r'^admin/',include(admin.site.urls)),
   
    url(r'new',HN_Views.get_new_content),
    url(r'history',HN_Views.history),
    url(r'suggested',HN_Views.similar),
    url(r'about',HN_Views.about),
    url(r'feedback',HN_Views.feedback),
    url(r'del',HN_Views.delkeep),
    
	url(r'^$',HN_Views.db_index),
    url(r'(?P<item>\w+)/(?P<item2>\d{1,})$',HN_Views.db_write),
    url(r'(?P<id>\w+)$',HN_Views.db_index),
    
    ]




