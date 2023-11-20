from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Songs(models.Model):
    EMOTION_CHOICES = [
        ('happy', 'Happy'),
        ('bright', 'Bright'),
        ('fun', 'Fun'),
        ('angry', 'Angry'),
        ('aggressive', 'Aggressive'),
        ('sad', 'Sad'),
        ('bitter', 'Bitter'),
        ('relaxed', 'Relaxed'),
        ('lonely', 'Lonely'),
        ('energetic', 'Energetic'),
        ('soothing', 'Soothing'),
        ('peacefull', 'Peacefull'),
        ('soft', 'Calm'),
        
    ]

    emotion = models.CharField(max_length=20, choices=EMOTION_CHOICES)
    songName = models.TextField(max_length=100)
    artist = models.TextField(max_length=100)
    coverImage = models.URLField()
    audioFile = models.FileField(upload_to='songs/')
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.songName
    

    

    
    