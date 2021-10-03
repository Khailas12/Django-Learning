from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField(blank=False, null=True)
    written_by = models.TextField(blank=False, null=True)