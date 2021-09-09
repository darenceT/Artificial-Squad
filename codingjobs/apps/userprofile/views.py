from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from apps.job.models import Application

@login_required
def dashboard(request):
	return render(request, 'userprofile/dashboard.html', {'userprofile': request.user.userprofile})

@login_required
def view_application(request, application_id):
    if request.user.userprofile.is_employer:
        application = get_object_or_404(Application, pk=application_id, job__created_by=request.user)
    else:
        application = get_object_or_404(Application, pk=application_id, created_by=request.user)
    
    return render(request, 'userprofile/view_application.html', {'application': application})
