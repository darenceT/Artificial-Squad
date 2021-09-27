from django import forms

from .models import Profile

class Profile_form(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['full_name', 'relevant_background', 'values', 'career_goals']