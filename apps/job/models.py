from django.contrib.auth.models import User
from django.db import models

class Job(models.Model):
	title = models.CharField(max_length=255) 	# will display as Title (any_how -> Any How)
	location = models.CharField(max_length=255, blank=True, null=True)
	description = models.TextField()
	requirements = models.TextField(blank=True, null=True)
	product_management = models.BooleanField(default=False)
	web_development = models.BooleanField(default=False)
	user_experience = models.BooleanField(default=False)
	marketing = models.BooleanField(default=False)
	finance = models.BooleanField(default=False)

	created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
	created_at = models.DateField(auto_now_add=True)
	changed_at = models.DateField(auto_now=True)

	def __str__(self):
		return self.title

class Application(models.Model):
	job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
	work_history = models.TextField()
	education = models.TextField()
	projects = models.TextField()

	created_by = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	# def __str__(self):	# does not work on click
	# 	return self.full_name
