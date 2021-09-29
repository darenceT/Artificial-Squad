from django.shortcuts import render
# from apps.userprofile.models import skills

def ai_jobs(request):

    # if userprofile.skills == jobs.skills:
    	# {{ jobs.title }}
    	# {{ job.description }}
    	# <a href="{% url %}">job detail</a>

    	# print(os.link(page,))

    return render(request, 'ai/ai_jobs.html')
