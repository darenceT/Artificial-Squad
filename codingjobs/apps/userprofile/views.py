from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage

from apps.job.models import Application, Job
from .models import Profile
from .forms import Profile_form

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

@login_required #FIXME test, is this necessary?
def ai_jobs(request):
    jobs = Job.objects.all()[0:3]
    return render(request, 'userprofile/ai_jobs.html', {'jobs': jobs})

# need @login_required here?
def profile(request):
    profile = get_object_or_404(Profile)
    return render(request, 'userprofile/profile.html', {'profile': profile})

def profile_create(request):
	if request.method == 'POST':
		form = Profile_form(request.POST)

		if form.is_valid():
			profile = form.save(commit=False)
			profile.created_by = request.user
			profile.save()

			return redirect('dashboard')
	else:
		form = Profile_form()

	return render(request, 'userprofile/profile_create.html', {'form': form})

@login_required #FIXME test, is this necessary?
def resume(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['resume']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)                  # FIXME bypassed on resume.html
        context['url'] = fs.url(name)       # FIXME bypassed on resume.html
        context['name'] = name
        # context['upload_time'] =          FIXME insert timestamp
    return render(request, 'userprofile/resume.html', context)