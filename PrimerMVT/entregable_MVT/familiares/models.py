from django.db import models

class Familiares(models.Model):
    name = models.CharField(max_length=50)
    birth_year= models.FloatField()
    zodiac_sign=models.CharField(max_length=50)
    is_adult=models.BooleanField()


# Create your models here.
