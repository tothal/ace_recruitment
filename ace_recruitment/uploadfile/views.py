from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Document
from .forms import DocumentForm


# Create your views here.
def form(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = DocumentForm()
	return render(request, 'uploadfile/form.html',{ 'form' : form})
#def model_form_upload(request):
#    if request.method == 'POST':
#        form = DocumentForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('home')
#    else:
#        form = DocumentForm()
#    return render(request, 'uploadfile/model_form_upload.html', {
#        'form': form
#    })
	
def home(request):
    documents = Document.objects.all()
    return render(request, 'ace/index.html', { 'documents': documents })
