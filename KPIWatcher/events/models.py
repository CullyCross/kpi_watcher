from django.contrib.auth.models import User
from django.db import models

from django.utils import timezone


class Company(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=250)
    description = models.TextField()

class Event(models.Model):
    creator = models.ForeignKey(User)
    name = models.CharField(max_length=250)
    text = models.TextField()
    date_published = models.DateTimeField(default=timezone.now, editable=False)
    subscribers = models.ManyToManyField(User, related_name="events")
    # create publish method in views.py

    def __str__(self):
        return self.name
