from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Beverages(models.Model):
    title = models.CharField(max_length=200, unique=True)
    type = models.CharField()
    cost = models.FloatField()
    calories = models.IntegerField()
    vegetarian = models.BooleanField()
    vegan = models.BooleanField()
    gluten = models.BooleanField()

class Food(models.Model):
    title = models.CharField(max_length=200, unique=True)
    type = models.CharField()
    cost = models.FloatField()
    calories = models.IntegerField()
    vegetarian = models.BooleanField()
    vegan = models.BooleanField()
    gluten = models.BooleanField()