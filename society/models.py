from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Group(models.Model):
	name = models.CharField(max_length=100)
	members = models.IntegerField()
	description = models.TextField()
	category =models.TextField()
	website_url= models.URLField(max_length=200)
	def __str__(self):
		return self.name

class Event(models.Model):
	description= models.TextField()
	creator_name = models.CharField(max_length=100)
	start_time = models.DateField()
	end_time = models.DateField()
	location =models.CharField(max_length=100)
	event_title =models.CharField(max_length=100)
	def __str__(self):
		return self.event_title

class People(models.Model):
	about_me =models.CharField(max_length=100)
	birth_date = models.DateField()
	fav_movies = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	photo_url =models.URLField(max_length=200)
	def __str__(self):
		return self.username

class NewUser(models.Model):
	user_name = models.CharField(unique = True, max_length=100)
	pass_word = models.CharField(max_length=100)
	def __str__(self):
		return self.user_name




