from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from .views import dashboard, view_application, ai_jobs, resume, profile, profile_create
from .views import *

urlpatterns = [
	path('', dashboard, name='dashboard'),
	path('application/<int:application_id>/', view_application, name='view_application'),
	path('ai_job/', ai_job, name='ai_job'),
	path('profile/', profile, name='profile'),
	path('profile_create/', profile_create, name='profile_create'),
	path('resume/', resume, name='resume'),
]
	# path('<int:profile_id>/', profile, name='profile'),
	# path('<int:profile_id>/profile_create/', profile_create, name='profile_create'),
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)