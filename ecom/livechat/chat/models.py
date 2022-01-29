from django.db import models
from datetime import datetime

class Room(models.Model):
    name = models.CharField(max_length=100)

class Message(models.Model):
    value = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)
    room = models.CharField(max_length=100)
    user = models.CharField(max_length=100)