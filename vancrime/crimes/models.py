from django.db import models

# Create your models here.

class crime(models.Model):
    cType = models.CharField(max_length=122)
    year = models.IntegerField(null=True)
    month = models.IntegerField(null=True)
    day = models.IntegerField(null=True)
    hour = models.IntegerField(null=True)
    minute = models.IntegerField(null=True)
    hundredBlock = models.CharField(max_length=122, null=True)
    neighbourhood = models.CharField(max_length=122, null=True)
    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)