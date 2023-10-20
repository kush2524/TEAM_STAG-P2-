from django.db import models

# Create your models here.
class sign(models.Model):
    username = models.CharField(max_length=100)
    venue = models.CharField(max_length=500)
    time = models.CharField(max_length=500)
    
