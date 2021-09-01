from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def frontpage(request):
	return render(request, 'core/frontpage.html')

def signup(request):
	form = UserCreationForm()
	return render(request, 'core/signup.html', {'form': form})