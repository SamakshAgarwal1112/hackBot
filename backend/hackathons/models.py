from django.db import models

# Create your models here.
class ScrapedHackathon(models.Model):
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=100)
    url = models.URLField()
    location = models.CharField(max_length=255)
    mode = models.CharField(max_length=255)
