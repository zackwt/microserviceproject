# Create your models here.
from django.db import models

class MyModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # add more fields as needed