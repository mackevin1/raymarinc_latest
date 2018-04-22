from django.contrib import admin

# Register your models here.
from .models import Board, Topic, BNShome, Homepage

admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(BNShome)
admin.site.register(Homepage)
