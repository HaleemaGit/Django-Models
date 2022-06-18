from django.conf import settings
from django.db import models


# Create your models here.
class PostApp(models.Model):
    '''a model for a blog post'''
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
