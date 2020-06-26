from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    dot = models.DateTimeField()
    summary = models.TextField()
    def __str__(self):
        return self.title
