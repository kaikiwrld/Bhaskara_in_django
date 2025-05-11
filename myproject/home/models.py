from django.db import models

# Create your models here.
class Bhaskara(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()
    delta = models.IntegerField()
    x1 = models.FloatField(null=True, blank=True)
    x2 = models.FloatField(null=True, blank=True)