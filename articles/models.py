from django.db import models


class Article(models.Model):
    source_id = models.SlugField(max_length=80, null=True, blank=True)
    source_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField()
    url = models.URLField()
    url_to_image = models.URLField()
    published_at = models.DateTimeField()
    content = models.TextField()

    class Meta:
        ordering = ("-published_at",)
