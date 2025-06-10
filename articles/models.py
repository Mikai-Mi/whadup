from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50] + '...'