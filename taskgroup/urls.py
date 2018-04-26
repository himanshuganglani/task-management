from django.conf.urls import url, include
from django.contrib import admin
from .views import register
from taskgroup import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^register/', views.register,name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^tasklist$', views.task, name='tasklist'),
    url(r'^createtask$', views.createtask, name='createtask'),
    url(r'^deletetask/(?P<tname>\d+)/$', views.deletetask, name='deletetask'),
    url(r'^login/', views.login, name='login'),
    

]