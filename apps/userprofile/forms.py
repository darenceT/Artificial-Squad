from django import forms

from .models import User_profile

class Profile_form(forms.ModelForm):
	class Meta:
		model = User_profile
		fields = ('full_name', 'relevant_background', 'values', 'career_goals',
				'product_management', 'web_development', 'user_experience',
				'marketing', 'finance')
