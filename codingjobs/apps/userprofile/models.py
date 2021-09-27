from django.contrib.auth.models import User
from django.db import models

class User_profile(models.Model):
	user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
	is_employer = models.BooleanField(default=False)

User.userprofile= property(lambda u:User_profile.objects.get_or_create(user=u)[0])

class Profile(models.Model):
	full_name = models.CharField(max_length=255)
	relevant_background = models.TextField()
	values = models.TextField()
	career_goals = models.TextField()
	
	# created_by = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):	# does not work on click
		return self.full_name