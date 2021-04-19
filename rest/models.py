from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField(max_length=100)
    image = models.ImageField(unique=False, blank=True)
    description = models.CharField(max_length=100)