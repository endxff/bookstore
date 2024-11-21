from django.db import models

from .category import Category


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveBigIntegerField(null=True)
    active = models.BooleanField(default=True)
    categoriy = models.ManyToManyField(Category, blank=True)
