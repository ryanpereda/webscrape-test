from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, blank=True)
    scraped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}: {self.text[:50]}"


class ScrapeState(models.Model):
    last_scraped_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Last scraped: {self.last_scraped_at}"