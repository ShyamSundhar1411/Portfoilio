from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    dot = models.DateField()
    summary = RichTextUploadingField()
    def __str__(self):
        return self.title
