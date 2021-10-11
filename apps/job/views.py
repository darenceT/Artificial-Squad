from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import Add_job_form, Application_form
from .models import Job, Application

def job_detail(request, job_id):
	job = Job.objects.get(pk=job_id)

	return render(request, 'job/job_detailed.html', {'job': job})

@login_required
def apply_for_job(request, job_id):
	job = Job.objects.get(pk=job_id)	

	if request.method == 'POST':
		form = Application_form(request.POST)

		if form.is_valid():
			application = form.save(commit=False)
			application.job = job
			application.created_by = request.user
			application.save()

			return redirect('dashboard')
	else:
		form = Application_form()

	return render(request, 'job/apply_for_job.html', {'form': form, 'job': job})

@login_required
def add_job(request):
	if request.method == 'POST':
		form = Add_job_form(request.POST)

		if form.is_valid():
			job = form.save(commit=False)
			job.created_by = request.user
			job.save()

			return redirect('dashboard')
	else:
		form = Add_job_form()

	return render(request, 'job/add_job.html', {'form': form})