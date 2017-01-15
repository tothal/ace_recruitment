from django.db import models

class Document(models.Model):
	name = models.CharField(max_length=45, blank=True)
	phone = models.CharField(max_length=15, blank=True)
	profession = models.CharField(max_length=45, blank=True)
	document = models.FileField(upload_to='documents/')
	uploaded_at = models.DateTimeField(auto_now_add=True)