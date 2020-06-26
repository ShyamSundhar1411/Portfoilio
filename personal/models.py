from django.db import models
class Project(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'images/')
    descriptionn = models.CharField(max_length = 250)
    url = models.URLField(blank = True)
    def __str__(self):
        return self.title
