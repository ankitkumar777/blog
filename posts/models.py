from django.db import models
from datetime import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    img = models.ImageField(upload_to ='uploads/', blank=True, null = True)
    last_modified = models.DateTimeField(auto_now=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True , blank=True)

    def __str__(self):
        return self.title
    