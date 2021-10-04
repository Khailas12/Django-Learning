from django.db import models

# Create your models here.
class Final(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=False)
    by = models.TextField(blank=False)