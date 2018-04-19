from django.contrib import admin
from bns.models import Project, ProjectType, Client, ProjectImages, Role

admin.site.register(Project)
admin.site.register(ProjectType)
admin.site.register(ProjectImage)
admin.site.register(Client)
admin.site.register(Role)
