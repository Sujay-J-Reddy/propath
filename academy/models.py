from django.db import models

# Create your models here.
class Birthdays(models.Model):
    name = models.CharField(max_length=255)
    franchise = models.CharField(max_length=255)
    birthday = models.DateField()

    def __str__(self):
        return  f"{self.name}'s Birthday"

class Schools(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)

class SchoolStudents(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(Schools,on_delete=models.CASCADE)
    level = models.CharField(max_length=50)
    dob = models.DateField()
    contact = models.CharField(max_length=20)


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

class CompetitionResults(models.Model):
    name =  models.CharField(max_length=100)
    franchisee = models.CharField(max_length=100)
    score = models.PositiveIntegerField()
    max_score = models.PositiveIntegerField()
    rank = models.PositiveIntegerField()

class TrainingDate(models.Model):
    name = models.CharField(max_length=255)
    training_level = models.PositiveIntegerField()
    franchise = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}'s level {self.training_level} training due"
    
class Enquiry(models.Model):
    STUDENT = 'Student'
    FRANCHISEE = 'Franchisee'
    TEACHER = 'Teacher'

    ENQUIRY_TYPE_CHOICES = [
        (STUDENT, 'Student'),
        (FRANCHISEE, 'Franchisee'),
        (TEACHER, 'Teacher'),
    ]

    COUNTRY_CODES = [
        ('+1', '+1 (United States)'),
        ('+44', '+44 (United Kingdom)'),
        ('+91', '+91 (India)'),
        ('+86', '+86 (China)'),
        ('+81', '+81 (Japan)'),
        ('+49', '+49 (Germany)'),
        ('+7', '+7 (Russia)'),
        ('+55', '+55 (Brazil)'),
        ('+33', '+33 (France)'),
        ('+39', '+39 (Italy)'),
        ('+82', '+82 (South Korea)'),
        # Add more country codes as needed
    ]

    name = models.CharField(max_length=255)
    mail = models.EmailField()
    type = models.CharField(max_length=255, choices=ENQUIRY_TYPE_CHOICES)
    phone_country_code = models.CharField(max_length=5, choices=COUNTRY_CODES)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=255)
    pin = models.CharField(max_length=10)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)  
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Events(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    photo = models.ImageField(upload_to='event_photos/')  
    details = models.TextField()