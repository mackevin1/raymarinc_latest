import math
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator

class homepage(models.Model):
    headline1 = models.CharField(max_length=250)
    backimage = models.FileField(null=True, blank=True)
    description = models.TextField(blank=True)
    headline = models.TextField(blank=True)
    subhead = models.TextField(blank=True)

    def __str__(self):
        return self.name


class bns_home(models.Model):
    title = models.CharField(max_length=250)
    image = models.FileField(null=True, blank=True)
    description = models.TextField(blank=True)
    headline = models.TextField(blank=True)
    subhead = models.TextField(blank=True)
    def __str__(self):
        return self.name
