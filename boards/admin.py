from django.contrib import admin

# Register your models here.
from .models import Board, Topic

admin.site.register(Board)
admin.site.register(Topic)
