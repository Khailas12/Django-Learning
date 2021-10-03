from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField(blank=False, null=True)
    written_by = models.TextField(blank=False, null=True)
    
    def absolute_url(self, *args, **kwargs):
        return reverse('article:article-detail', kwargs={'id': self.id})