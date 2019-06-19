from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.DecimalField()
    times_read = models.IntegerField()
    published_on = models.DateTimeField(auto_now=True, auto_now_add=False)
