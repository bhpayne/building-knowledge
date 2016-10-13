from django.contrib import admin
# Register your models here.
from . models import ycombinator 
from . models import stories
from . models import base_model
from . models import similar_articles
from . models import feedback
from . models import test
from . models import comments
class ycombinatorAdmin(admin.ModelAdmin):
	list_display= ['ip_address','parsed_user_agent','time_stamp']
	list_per_page = 400
admin.site.register(ycombinator,ycombinatorAdmin)


class storiesAdmin(admin.ModelAdmin):
	list_display= ['ID','author','points','comments','domain']
	list_per_page = 400
admin.site.register(stories,storiesAdmin)


class base_modelAdmin(admin.ModelAdmin):
	list_display= ['author','points','comments','domain']
	list_per_page = 400
admin.site.register(base_model,base_modelAdmin)


class similar_articlesAdmin(admin.ModelAdmin):
	list_display= ['article1','article2','score']
	list_per_page = 400
	search_fields = ('article1','article2','score')
admin.site.register(similar_articles,similar_articlesAdmin)


class testAdmin(admin.ModelAdmin):
	
	list_display= ['name','email','feedback']
	list_per_page = 400
admin.site.register(test,testAdmin)


class commentsAdmin(admin.ModelAdmin):
	
	list_display= ['name','email','feedback']
	list_per_page = 400
admin.site.register(comments,commentsAdmin)
