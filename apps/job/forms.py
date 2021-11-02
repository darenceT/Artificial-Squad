from django import forms

from .models import Job, Application

class Add_job_form(forms.ModelForm):
	class Meta:
		model = Job
		fields = ('title', 'location', 'description', 'requirements', 
			'product_management', 'web_development', 'user_experience',
			'marketing', 'finance')

class Application_form(forms.ModelForm):
	class Meta:
		model = Application
		fields = ('work_history', 'education', 'projects')