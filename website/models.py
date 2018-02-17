from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class List(models.Model):
    user = models.ForeignKey(User, related_name="owner", on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=300, default="your list")


class Item(models.Model):
    text = models.TextField()
    date = models.DateField()
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    marked  = models.BooleanField(default=True)