from datetime import datetime
from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
class Students(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    franchise = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='student_photos/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])], null=True, blank=True, max_length=255)
    course = models.CharField(max_length=20, choices=[('abacus', 'Abacus'), ('vedic_maths', 'Vedic Maths'),('handwriting', 'Handwriting'),], null=True)
    programme = models.CharField(max_length=10, choices=[('junior', 'Junior'), ('senior', 'Senior')], null=True)
    level = models.IntegerField()
    dob = models.DateField()
    contact = models.CharField(max_length=20)
    sex = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], null=True)
    father_name = models.CharField(max_length=100, null=True)
    father_occupation = models.CharField(max_length=100, null=True)
    mother_name = models.CharField(max_length=100, null=True)
    mother_occupation = models.CharField(max_length=100, null=True)
    qualification = models.CharField(max_length=100, null=True)
    reference_by = models.CharField(max_length=20, choices=[('paper_ads', 'Paper Ads'), ('parents', 'Parents'), ('social_media', 'Social Media'), ('others', 'Others')], null=True)
    residential_address = models.TextField(null=True)
    contact_number = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    school_name = models.CharField(max_length=100, null=True)
    standard = models.CharField(max_length=50, null=True)
    num_siblings = models.IntegerField(null=True)
    join_date = models.DateField(auto_now_add=True)
    course_start_date = models.DateField(null=True)
    dropped = models.BooleanField(default=False)

    @property
    def age(self):
        today = datetime.now().date()
        dob = self.dob
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def __str__(self):
        return f"{self.id} - {self.name}"


    