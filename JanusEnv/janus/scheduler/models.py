from django.db import models
import datetime

# Create your models here.

class SchedulerConfig(models.Model):
    param = models.CharField(max_length=30)
    value = models.CharField(max_length=255)
    datatype = models.CharField(max_length=20)
    mod_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.param


class Test(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField()
    weight = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.name


class Resource(models.Model):
    available = models.BooleanField(default=True)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    ipv4 = models.CharField(max_length=15)

    def __str__(self):
        return self.name
