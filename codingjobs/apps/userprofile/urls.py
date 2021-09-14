from django.urls import path, include

from .views import dashboard, view_application, ai_jobs

urlpatterns = [
	path('', dashboard, name='dashboard'),
	path('application/<int:application_id>/', view_application, name='view_application'),
	path('ai_jobs/', ai_jobs, name='ai_jobs'),
]