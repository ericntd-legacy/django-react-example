from django.db import models

# Create your models here.
class Comment(models.Model):
    comment_text = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
