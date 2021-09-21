from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from apps.job.models import Application, Job

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

@login_required
def ai_jobs(request):
    jobs = Job.objects.all()[0:3]

    return render(request, 'userprofile/ai_jobs.html', {'jobs': jobs})

@login_required
def resume(request):

    return render(request, 'userprofile/resume.html')