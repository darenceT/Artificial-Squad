from django.shortcuts import render


def ai_jobs(request):
    # jobs = Job.objects.all()[0:3]
    return render(request, 'ai/ai_jobs.html')
