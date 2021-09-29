from django import forms

from .models import Profile

class Profile_form(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('full_name', 'relevant_background', 'values', 'career_goals')
	product_management = forms.BooleanField(required=False)
	web_developement = forms.BooleanField(required=False)
	user_experience = forms.BooleanField(required=False)
	marketing = forms.BooleanField(required=False)
	finance = forms.BooleanField(required=False)