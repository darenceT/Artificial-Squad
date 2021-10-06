from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

class User_profile(models.Model):
	user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
	is_employer = models.BooleanField(default=False)
	resume = models.ImageField(default='default.jpg', upload_to='resume')
	full_name = models.CharField(max_length=255, default='Enter full name')
	relevant_background = models.TextField()
	values = models.TextField()
	career_goals = models.TextField()
	
	# created_by = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)
	# created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):	
		# return self.full_name
		return f'{self.user.username} Profile'
	
User.userprofile= property(lambda u:User_profile.objects.get_or_create(user=u)[0])
