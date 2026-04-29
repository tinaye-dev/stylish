from django.db import models

# Create your models here.

class Soccerclub(models.Model):
    club_name = models.CharField(max_length=50)
    club_location = models.CharField(max_length=45)
    club_manager = models.CharField(max_length=50) 