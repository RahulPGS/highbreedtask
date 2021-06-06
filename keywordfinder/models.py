from django.db import models


# Create your models here.

class URLKeywords(models.Model):
    url = models.URLField()
    keywords = models.TextField(null=True)
    description = models.TextField(null=True)
    og_description = models.TextField(null=True)