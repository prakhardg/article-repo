from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100, unique=True, db_index=True)
    content = models.TextField(default= "content cannot be shown")
    rating = models.DecimalField(max_digits=10, decimal_places=4)
    times_read = models.IntegerField(default=0)
    published_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    readkey = models.TextField()

    def __str__(self):
        return self.title



