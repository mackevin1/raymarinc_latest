from django.contrib import admin

# Register your models here.
from .models import Board, Category, ProductImages

admin.site.register(Board)
admin.site.register(Category)
admin.site.register(ProductImages)
