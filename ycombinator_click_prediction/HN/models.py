from __future__ import unicode_literals

# Create your models here.

# Create your models here.
from django.db import models
# Create your models here.
from django.utils import timezone
# Create your models here.

class ycombinator(models.Model):
	comments= models.CharField(max_length=200,blank=True)
	points= models.CharField(max_length=5,blank=True)
	time= models.CharField(max_length=200,blank=True)
	title= models.CharField(max_length=200,blank=True)
	author= models.CharField(max_length=200,blank=True)
	
	user_agent = models.CharField(max_length=200)	
	url_clicked_on= models.CharField(max_length=350,blank=True)
	time_stamp= models.CharField(max_length=200,blank=True)
	ip_address=models.CharField(max_length=20,blank=True)
	parsed_user_agent=models.CharField(max_length=200,blank=True)
	domains= models.CharField(max_length=200,blank=True)
	article= models.CharField(max_length=200,blank=True)


class stories(models.Model):
	comments=models.IntegerField(blank=True)
	points=models.IntegerField(blank=True)
	time=models.CharField(max_length=350,blank=True)
	title=models.CharField(max_length=350,blank=True)
	author=models.CharField(max_length=350,blank=True)
	ID=models.CharField(max_length=350,unique=True)
	url=models.CharField(max_length=350,blank=True)
	domain=models.CharField(max_length=350,blank=True)
	


class base_model(models.Model):
	article=models.CharField(max_length=200,blank=True)
	author=models.CharField(max_length=350,blank=True)
	comments= models.CharField(max_length=200,blank=True)
	domain=models.CharField(max_length=350,blank=True)
	ip_address=models.CharField(max_length=20,blank=True)
	parsed_user_agent=models.CharField(max_length=200,blank=True)
	points=models.IntegerField(blank=True)
	time=models.CharField(max_length=350,blank=True)
	time_stamp= models.CharField(max_length=200,blank=True)
	title=models.CharField(max_length=350,blank=True)
	url=models.CharField(max_length=350,blank=True)
	url_clicked_on= models.CharField(max_length=350,blank=True)
	user_agent = models.CharField(max_length=200)	
	suggestions= models.TextField(blank=True)

class similar_articles(models.Model):
	article1=models.CharField(max_length=200,blank=True)
	article2=models.CharField(max_length=200,blank=True)
	score=models.DecimalField(max_digits=20, decimal_places=5)

class feedback(models.Model):
	name = models.CharField(max_length=100,blank=True)
	email = models.CharField(max_length=100,blank=True)
	feedback = models.TextField()
	

class test(models.Model):
	name = models.CharField(max_length=100,blank=True)
	email = models.CharField(max_length=100,blank=True)
	feedback = models.TextField()

class comments(models.Model):
	name = models.CharField(max_length=100,blank=True)
	email = models.CharField(max_length=100,blank=True)
	feedback = models.TextField()


class moreless(models.Model):
    more = models.BooleanField()
    less = models.BooleanField()