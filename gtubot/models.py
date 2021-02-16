from django.db import models

# Create your models here.

class Circular(models.Model):
    news = models.CharField(max_length=5000)
    