from django.db import models

# Create your models here.
class ScrapedHackathon(models.Model):
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=100,null=True)
    url = models.URLField(null=True)
    location = models.CharField(max_length=255,null=True)
    mode = models.CharField(max_length=255,null=True)
