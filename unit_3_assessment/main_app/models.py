from django.db import models

# Create your models here.
class Widgets(models.Model):
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()