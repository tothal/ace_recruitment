from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index,name = 'index'),
	url(r'^about_us/$', views.about_us, name = 'about'),
	url(r'^contact/$', views.contact, name = 'contact'),
	url(r'for_jobseekers/$', views.for_jobseekers, name = 'for_jobseekers'),
	url(r'^jobs/$', views.jobs, name = 'jobs'),
	url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
	]