from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Forum(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=200, blank=True, default='')
    created = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
        
class Topic(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=10000, blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    forum = models.ForeignKey(Forum, related_name='topics')
    
    def __str__(self):
        return self.title
        
class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField(max_length=10000, blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic, related_name='posts')
    
    def __str__(self):
        return self.title
