from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length is important
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000000)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(null=True)   # null=True or default=True
    # null -> purely database-related
    # blank -> validation-related. If a field has blank=True , form validation will allow entry of an empty value. If a field has blank=False, the field will be required.
