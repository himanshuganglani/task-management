from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

	

class User(AbstractBaseUser):
	email = models.EmailField(max_length=40, unique=True) 
	USERNAME_FIELD = 'email'
	password = models.CharField(max_length=50)
	
	def __str__(self):
		return self.email
	def __str__(self):
		return self.password


class TaskModel(models.Model):
	
	Name = models.CharField(max_length=100)
	Description = models.CharField(max_length=100,)
	StartTime = models.DateField(auto_now_add=False, blank=True)     
	EndTime = models.DateField(auto_now_add=False, blank=True)
	Status = models.CharField(max_length=100)

	def __unicode__(self):
		return "{0} {1} {2} {3} {4}".format(
			self.Name, self.Description, self.StartTime,
    		self.EndTime, self.Status)