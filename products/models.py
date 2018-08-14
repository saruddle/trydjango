from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    