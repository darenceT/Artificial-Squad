from django.contrib.auth.models import User
from django.db import models

class User_profile(models.Model):
	user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
	is_employer = models.BooleanField(default=False)
	resume = models.ImageField(default='default.jpg', upload_to='resume')
	full_name = models.CharField(max_length=255, default='Enter full name')
	relevant_background = models.TextField()
	product_management = models.BooleanField(default=False)
	web_developement = models.BooleanField(default=False)
	user_experience = models.BooleanField(default=False)
	marketing = models.BooleanField(default=False)
	finance = models.BooleanField(default=False)
	values = models.TextField()
	career_goals = models.TextField()
	
	
	# created_by = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)
	# created_at = models.DateTimeField(auto_now_add=True)

	# 3 options
	def __str__(self):		 
		# return self.full_name
		# return f'{self.user.username}\'s profile'
		return f'{self.full_name} ({self.user.username}) profile'
	
User.userprofile= property(lambda u:User_profile.objects.get_or_create(user=u)[0])
