
from django.db import models

class Post(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=300, null=True, blank=True)
    body = models.TextField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.title
