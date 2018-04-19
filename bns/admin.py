from django.contrib import admin
from bns.models import Project, ProjectType, Client, ProjectImages, Role

admin.site.register(Project)
admin.site.register(ProjectType)
admin.site.register(ProjectImages)
admin.site.register(Client)
admin.site.register(Role)
