from django.http import HttpRequest
from django.shortcuts import render
from application.models import Member
import logging

	
# Standard instance of a logger with __name__
stdlogger = logging.getLogger(__name__)

# Custom instance logging with explicit name
dbalogger = logging.getLogger('dba')

def home(request):
	#render the home page, which is basically go to the top of the index.html
	assert(isinstance(request, HttpRequest))
	
	info = dict()
	info['presentMembers'] = Member.objects.filter(alumni = False)
	
	return render(request, 'application/index.html', info)
