#from django.conf.urls.defaults import *
from bns.models import Project

info_dict = {
    'queryset': Project.objects.all(),
}

urlpatterns = [
    url(r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    url(r'^(?P<slug>[\w-]+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
]
