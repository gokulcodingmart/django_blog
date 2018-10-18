from django.conf.urls import  url
from . import views



urlpatterns = [
	url(r'^about/$', views.about, name='about' ),
	url(r'^contact/$', views.contact, name='contact' ),
	url(r'^business/$', views.business, name='business' ),
	url(r'^education/$', views.education, name='education' ),
	url(r'^comment/$', views.comment, name='comment' ),


	url(r'^index/$', views.index, name='index' ),
   
   ]