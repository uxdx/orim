from pydoc import describe
from statistics import mode
from turtle import title
from unicodedata import category
from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100, blank=True, null=False)
    publishedAt = models.DateTimeField()
    channelTitle = models.CharField(max_length=100, blank=True, null=False)
    categoryId = models.IntegerField()
    thumbnail_url = models.CharField()

    def __str__(self) -> str:
        return self.title

class Channel(models.Model):
    name = models.CharField(max_length=50, null=False)
    describer = models.IntegerField()

    def __str__(self) -> str:
        return self.name