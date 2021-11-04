from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
	path('', dashboard, name='dashboard'),
	path('application/<int:application_id>/', view_application, name='view_application'),
	path('ai_job/', ai_job, name='ai_job'),
	path('browse_jobs/', browse_jobs, name='browse_jobs'),
	path('profile/', profile, name='profile'),
	path('profile_create/', profile_create, name='profile_create'),
	path('resume/', resume, name='resume'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)