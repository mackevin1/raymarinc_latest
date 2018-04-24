import math
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator


class Homepage(models.Model):
    headline1 = models.CharField(max_length=250)
    backimage = models.FileField(null=True, blank=True)
    description = models.TextField(blank=True)
    headline = models.TextField(blank=True)
    subhead = models.TextField(blank=True)
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name

class introduction(models.Model):
    headline = models.TextField(blank=True)
    subhead = models.TextField(blank=True)
    backimage = models.FileField(null=True, blank=True)
    description = models.TextField(blank=True)
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name


class BNShome(models.Model):
    title = models.CharField(max_length=250)
    image = models.FileField(null=True, blank=True)
    description = models.TextField(blank=True)
    headline = models.TextField(blank=True)
    subhead = models.TextField(blank=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class ProductImages(models.Model):
    name = models.CharField(max_length=100)
    images = models.FileField(null=True, blank=True)
    primary = models.FileField(null=True, blank=True)
    category = models.ManyToManyField(Category, through='Board')

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
    headline = models.CharField(max_length=250)
    subhead = models.CharField(blank=True, max_length=200)
    headlineabout = models.CharField(max_length=250)
    subheadabout = models.CharField(blank=True, max_length=200)
    bodyleftabout = models.TextField(blank=True, max_length=500)
    headlineleftabout = models.TextField(blank=True, max_length=1000)
    bodyrightabout = models.TextField(blank=True, max_length=500)
    headlinerightabout = models.TextField(blank=True, max_length=1000)
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
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
    images = models.ForeignKey(ProductImages, related_name='+', on_delete=models.CASCADE)
    image2 = models.FileField(null=True, blank=True)
    image3 = models.FileField(null=True, blank=True)
    image4 = models.FileField(null=True, blank=True)
    sectionbnsheadline = models.CharField(max_length=250)
    sectionbnssubhead = models.CharField(max_length=250)
    sectionbnsbody = models.TextField(blank=True, max_length=1000)
    sectionbnswireless = models.CharField(max_length=250)
    sectionbnscellular = models.CharField(max_length=250)
    imagebns1 = models.FileField(null=True, blank=True)
    imagebns2 = models.FileField(null=True, blank=True)
    imagebns3 = models.FileField(null=True, blank=True)
    imagebns4 = models.FileField(null=True, blank=True)
    sectionridrheadline = models.CharField(blank=True, max_length=250)
    sectionridrsubhead = models.CharField(blank=True, max_length=250)
    sectionridrbody = models.CharField(blank=True, max_length=1000)
    sectionridr1head = models.TextField(blank=True, max_length=250)
    sectionridr1 = models.CharField(blank=True, max_length=250)
    sectionridr2head = models.TextField(blank=True, max_length=250)
    sectionridr2 = models.CharField(blank=True, max_length=250)
    sectionridr3head = models.TextField(blank=True, max_length=250)
    sectionridr3 = models.CharField(blank=True, max_length=250)
    sectionridr4head = models.TextField(blank=True, max_length=250)
    sectionridr4 = models.CharField(blank=True, max_length=250)
    imageridr1 = models.FileField(null=True, blank=True)
    imageridr2 = models.FileField(null=True, blank=True)
    imageridr3 = models.FileField(null=True, blank=True)
    imageridr4 = models.FileField(null=True, blank=True)
    sectionnocheadline = models.CharField(blank=True, max_length=250)
    sectionnocsubhead = models.CharField(blank=True, max_length=250)
    sectionnocbody = models.CharField(blank=True, max_length=1000)
    sectionnoc1head = models.TextField(blank=True, max_length=250)
    sectionnoc1 = models.CharField(blank=True, max_length=1000)
    sectionnoc2head = models.TextField(blank=True, max_length=250)
    sectionnoc2 = models.CharField(blank=True, max_length=1000)
    sectionnoc3head = models.TextField(blank=True, max_length=250)
    sectionnoc3 = models.CharField(blank=True, max_length=1000)
    sectionnoc4head = models.TextField(blank=True, max_length=250)
    sectionnoc4 = models.CharField(blank=True, max_length=1000)
    imagenoc1 = models.FileField(null=True, blank=True)
    imagenoc2 = models.FileField(null=True, blank=True)
    imagenoc3 = models.FileField(null=True, blank=True)
    imagenoc4 = models.FileField(null=True, blank=True)


    def __str__(self):
        return self.name
    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE,)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE,)
    views = models.PositiveIntegerField(default=0)  # <- here

    def __str__(self):
        return self.subject

    def get_page_count(self):
        count = self.posts.count()
        pages = count / 20
        return math.ceil(pages)

    def has_many_pages(self, count=None):
        if count is None:
            count = self.get_page_count()
        return count > 6

    def get_page_range(self):
        count = self.get_page_count()
        if self.has_many_pages(count):
            return range(1, 5)
        return range(1, count + 1)

    def get_last_ten_posts(self):
        return self.posts.order_by('-created_at')[:10]

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE,)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE,)
    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)

def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))





class Products(models.Model):
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
    category = models.ManyToManyField(Category, through='Products')
    category = models.ForeignKey(Category, related_name='+', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Products, related_name='+', on_delete=models.CASCADE)
