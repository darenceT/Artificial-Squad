from django.shortcuts import render
from apps.job.models import Job
from apps.userprofile.models import User_profile


def ai_jobs(request):
	ai_jobs = {}
	for job in Job.objects.all():
		if job.product_management == User_profile.product_management:
			ai_jobs['product management'] = job
		elif job.web_development == User_profile.web_development:
			ai_jobs['web development'] = job
		elif job.user_experience == User_profile.user_experience:
			ai_jobs['user experience'] = job
		elif job.marketing == User_profile.marketing:
			ai_jobs['marketing'] = job
		elif job.finance == User_profile.finance:
			ai_jobs['finance'] = job
	
	return render(request, 'ai/ai_jobs.html', ai_jobs)

def ai_job(request):
    jobs = Job.objects.all()[0:3]
    return render(request, 'userprofile/ai_job.html', {'jobs': jobs})


def resume(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['resume']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)  # FIXME bypassed on resume.html
        context['url'] = fs.url(name)  # FIXME bypassed on resume.html
        context['name'] = name
    # context['upload_time'] =          FIXME insert timestamp
    return render(request, 'userprofile/resume.html', context)

# if userprofile.skills == jobs.skills:
    	# {{ jobs.title }}
    	# {{ job.description }}
    	# <a href="{% url %}">job detail</a>

    	# print(os.link(page,))