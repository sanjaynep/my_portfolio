from django.db import models
from django.core.exceptions import ValidationError
from django.contrib import messages



class message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    message = models.TextField()


    def __str__(self):
        return self.name

# Create your models here.
