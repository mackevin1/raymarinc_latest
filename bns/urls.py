from django.views.generic.list import ListView
from bns.models import Project
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from bns import views
from accounts import views as accounts_views
from boards import views as boards_views

info_dict = {
    'queryset': Project.objects.all(),
}

urlpatterns = [
    url(r'^bns/$', views.ProductListView.as_view(), info_dict),
    url(r'^bns(?P<slug>[\w-]+)/$', views.ProductListView.as_view(), info_dict),
]
