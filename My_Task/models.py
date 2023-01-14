from django.db import models

# Create your models here.

class Author(models.Model):
    """Handling the author model"""
    author=models.CharField(max_length=30)
    quoteIds=models.JSONField()


class Quote(models.Model):
    """Handling the Quote model"""
    quote=models.TextField()
    quoteId=models.IntegerField()
    
