from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse

from apps.job.models import Job
from apps.userprofile.models import User_profile

def frontpage(request):
	jobs = Job.objects.all()#[0:3]

	return render(request, 'core/frontpage.html', {'jobs': jobs})

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			user = form.save()

			account_type = request.POST.get('account_type', 'jobseeker')

			if account_type == 'employer':
				userprofile = User_profile.objects.create(user=user, is_employer=True)
				userprofile.save()
			else:
				userprofile = User_profile.objects.create(user=user)
				userprofile.save()

			login(request, user)

			return redirect('dashboard')
	form = UserCreationForm()
	return render(request, 'core/signup.html', {'form': form})

def about(request):
	return render(request, 'core/about.html')

def resources(request):
	return render(request, 'core/resources.html')

def careers(request):
	return render(request, 'core/careers.html')