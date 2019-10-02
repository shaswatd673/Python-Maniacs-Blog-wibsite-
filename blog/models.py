from django.db import models
from django.utils import timezone
#this is a utility class that will help us with the date_posted variable
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	#'auto_now' will update the date_posted variable everytime a post in updated
	#'auto_now_add' wll only update the date_posted at the creation of a new Post object
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	#notes for console
	#when queries require data from two table django provides
	#a command as 'modelobject.modelname_set'

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})