from django.http import HttpRequest
from django.shortcuts import render




def home(request):
	#render the home page, which is basically go to the top of the index.html
	assert(isinstance(request, HttpRequest))
	return render(request, 'application/index.html')
