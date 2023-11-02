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
    qty = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
class Quantity(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

class Logs(models.Model):
    vendor = models.CharField(max_length=100)
    items = models.JSONField()
    date = models.DateField()