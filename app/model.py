from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    
    labels = models.IntegerField(('labels'))
    uri = models.CharField(("uri"), max_length= 255 )