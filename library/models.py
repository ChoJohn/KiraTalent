from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=100, blank=False)
    quantity = models.IntegerField(default=0)
    is_reserved = models.BooleanField(default=False, null=True)