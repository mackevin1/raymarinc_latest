from django.contrib import admin

# Register your models here.
from .models import Board, Topic

admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(bns_home)
admin.site.register(homepage)
