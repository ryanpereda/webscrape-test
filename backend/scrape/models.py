from django.db import models


class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    scraped_at = models.DateTimeField(auto_now_add=True)


class ScrapeState(models.Model):
    last_scraped_at = models.DateTimeField(null=True, blank=True)