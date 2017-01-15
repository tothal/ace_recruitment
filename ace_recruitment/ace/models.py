from django.db import models

# Create your models here.
class Jobs(models.Model):
	pub_date = models.DateTimeField('date published')
	title = models.CharField(max_length=10000)
	short_description = models.CharField(max_length=999999)
	long_description = models.CharField(max_length=9999999999)
	company_name = models.CharField(max_length=1000)
	company_logo = models.ImageField(upload_to='logo')