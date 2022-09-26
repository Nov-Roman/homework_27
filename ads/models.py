from django.db import models


class Ad(models.Model):
    author = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=2000)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=None)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
