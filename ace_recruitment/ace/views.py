from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Jobs

# Create your views here.

def index(request):
	#return render(request, 'ace/index.html')
	#return HttpResponse("hello world")
	template = loader.get_template('ace/homepage.html')
	return HttpResponse(template.render(request))

def about_us(request):
	return render(request,'ace/about us.html')

def contact(request):
	return render(request,'ace/contact.html')

def for_jobseekers(request):
	return render(request,'ace/for jobseekers.html')
	
def jobs(request):
	jobs = Jobs.objects.all()
	context = {
		'jobs': jobs
	}
	return render(request,'ace/jobs.html',context)

def detail(request, id):
	job = get_object_or_404(Jobs, pk=id)
	context = {
		'job':job
	}
	return render(request,'ace/job page.html',context)