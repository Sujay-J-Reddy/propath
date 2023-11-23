from datetime import datetime
from django.db import models

# Create your models here.
class Students(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    franchise = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    dob = models.DateField()
    contact = models.CharField(max_length=20)

    @property
    def age(self):
        today = datetime.now().date()
        dob = self.dob
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def __str__(self):
        return f"{self.id} - {self.name}"


    