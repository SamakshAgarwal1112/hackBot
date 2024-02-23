from django.db import models

# Create your models here.

class Bookmark(models.Model):
    user = models.ForeignKey('auth.User',related_name='bookmarks',on_delete=models.CASCADE)
    scraped_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)