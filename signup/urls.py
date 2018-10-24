
from django.conf.urls import url, include
from django.contrib import admin
from .views import home, register, register_success, logout_page

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import *
urlpatterns = [
 	url(r'^$', auth_views.LoginView.as_view(), name='login'),
    url(r'^home/$', home),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(), name='login' ),
    url(r'^logout/$', logout_page),
]