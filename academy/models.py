from django.db import models

# Create your models here.
class Birthdays(models.Model):
    name = models.CharField(max_length=255)
    franchise = models.CharField(max_length=255)
    birthday = models.DateField()