from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
