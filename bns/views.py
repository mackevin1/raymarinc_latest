from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.template import Context

from .models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = 'Project'
    template_name = 'project.html'

def get_queryset(self):
    self.project = get_object_or_404(Object, pk=self.kwargs.get('pk'))
    queryset = self.object.order_by('-last_updated')
    return queryset
