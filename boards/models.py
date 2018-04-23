import math
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator



class Products(models.Model):
    companyname = models.CharField(max_length=100)
    images = models.FileField(null=True, blank=True)
    name = models.CharField(max_length=100)
    productid = models.CharField(max_length=100)
    tbipartnumber = models.TextField(max_length=100)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    value = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    searchkeys = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Images(models.Model):
    name = models.ForeignKey(Products, on_delete=models.CASCADE)
    images = models.ForeignKey(Products, on_delete=models.CASCADE)
    primary = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.ProductName

class Category(models.Model):
    name = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Products, on_delete=models.CASCADE)
