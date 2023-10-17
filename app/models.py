from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    
    labels = models.IntegerField()
    uri = models.CharField( max_length= 255 )