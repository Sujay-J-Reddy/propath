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

    birthday = models.DateField()

class LevelCertificates(models.Model):
    student = models.CharField(max_length=100)
    franchise = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    programme = models.CharField(max_length=100)
    level = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.franchise} - {self.course} - {self.programme} {self.level}"
    
class CompetitionRegister(models.Model):
    circular_no = models.CharField(max_length=100)
    franchise = models.CharField(max_length=100)
    students = models.TextField()
    date = models.DateField(auto_now_add=True)

class Competition(models.Model):
    circular_no = models.CharField(max_length=100,primary_key=True)
    level_cutoff_date = models.DateField()
    pdf_file = models.FileField(upload_to='competition_pdfs/')
