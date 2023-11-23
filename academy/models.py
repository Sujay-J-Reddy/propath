from django.db import models

# Create your models here.
class Birthdays(models.Model):
    name = models.CharField(max_length=255)
    franchise = models.CharField(max_length=255)
    birthday = models.DateField()

class Schools(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)

class SchoolStudents(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    franchise = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    dob = models.DateField()
    contact = models.CharField(max_length=20)

