from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class List(models.Model):
    user = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300, default="twoja lista", verbose_name="")

    def __str__(self):
        return "{0}".format(
             self.name)


class Item(models.Model):
    text = models.CharField(max_length=300, default="", verbose_name="")
    date = models.DateTimeField(auto_now=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="table_items")
    marked = models.BooleanField(default=True)
    price = models.DecimalField(default=0.0, decimal_places=2, verbose_name="", max_digits=20)

    def __str__(self):
        return "{0}".format(self.text)


