from django.db import models


# Create your models here.

class URLKeywords(models.Model):
    url = models.URLField()
    keywords = models.TextField()
    description = models.TextField()
    og_description = models.TextField()

    def __str__(self):
        return f"""
                url: {self.url}
                keywords: {self.keywords.split(',')}
                description: {self.description}
                og_description: {self.og_description}
                """
