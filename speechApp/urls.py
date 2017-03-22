from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('speechApp.views',
	url(r'^$', views.index, name='index'),
	url(r'^search/', views.search, name = 'search'),
	url(r'^profile/$', views.profile, name = 'profile'))