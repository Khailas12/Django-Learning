from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField(blank=False, null=True)
    writer_name = models.TextField(blank=False)
    
    
    def get_absolute_url(self, *args, **kwargs):
        return reverse('blog:blog-detail', kwargs={'id': self.id})