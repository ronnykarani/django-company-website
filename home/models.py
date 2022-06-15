from django.conf import settings
from django.db import models
from django.utils import timezone


class Team(models.Model):
    name = models.CharField(max_length=80)
    photo = models.ImageField(upload_to='team/')
    job = models.CharField(max_length=80, blank=True)
    description = models.TextField(max_length=150)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Testimony(models.Model):
    name = models.CharField(max_length=80)
    photo = models.ImageField(upload_to='testimony/')
    job = models.CharField(max_length=80, blank=True)
    text = models.TextField(max_length=150)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name