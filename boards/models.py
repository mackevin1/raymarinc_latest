import math
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator



class ProductImages(models.Model):
    name = models.CharField(max_length=100)
    images = models.FileField(null=True, blank=True)
    primary = models.FileField(null=True, blank=True)

    def __str__(self):
        if self.name==None:
            return "No Product Image"
        return self.name

class Category(models.Model):
    tbipartnumber = models.TextField(max_length=1000)
    name = models.TextField(max_length=1000)
    def __str__(self):
        if self.tbipartnumber==None:
            return "No category"
        return self.tbipartnumber


class Board(models.Model):
    companyname = models.CharField(max_length=100)
    images = models.ForeignKey(ProductImages, related_name='+', on_delete=models.CASCADE)
    name = models.ForeignKey(ProductImages, related_name='+', on_delete=models.CASCADE)
    productid = models.CharField(max_length=100)
    tbipartnumber = models.TextField(max_length=100)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    proddescription = models.TextField(max_length=1000)
    value = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    searchkeys = models.CharField(max_length=100)

    def __str__(self):
        if self.tbipartnumber==None:
            return "No product"
        return self.tbipartnumber


class SubCategory(models.Model):
    category = models.ManyToManyField(Category, through='Boards')
    category = models.ForeignKey(Category, related_name='+', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Board, related_name='+', on_delete=models.CASCADE)
