from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    dot = models.DateTimeField()
    summary = models.TextField()
    def dot_pretty(self):
        return self.dot.strftime('%b %e %Y')
    def __str__(self):
        return self.title
