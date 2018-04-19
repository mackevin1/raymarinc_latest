from django.views.generic.list import ListView, DetailView
from bns.models import Project
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

info_dict = {
    'queryset': Project.objects.all(),
}

urlpatterns = [
    url(r'^bns/$', django.views.generic.list.ListView, info_dict),
    url(r'^(?P<slug>[\w-]+)/$', django.views.generic.list.ListView, info_dict),
]
