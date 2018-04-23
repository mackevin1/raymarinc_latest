from django.contrib import admin

# Register your models here.
from .models import Board, Topic, BNShome, Homepage, introduction, Products, Category, ProductImages

admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(BNShome)
admin.site.register(Homepage)
admin.site.register(introduction)
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(ProductImages)
