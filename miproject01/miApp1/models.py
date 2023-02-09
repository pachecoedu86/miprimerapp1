from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length= 40)
    surname =models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.EmailField()

class favoriteSport(models.Model):
    sport = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

class favoriteColor(models.Model):
    color1 = models.CharField(max_length=30)
    color2 = models.CharField(max_length=30)

class favoriteCoach(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()


