from datetime import timedelta
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

class CustomUser(AbstractUser):
    ACCOUNT_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('franchisee', 'Franchisee'),
        ('teacher', 'Teacher'),
        ('student', 'Student')
    )
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)

    def save(self, *args, **kwargs):
        if self.account_type == 'admin':
            # Set is_staff and is_superuser to True for admin users
            self.is_staff = True
            self.is_superuser = True
        if self.is_superuser:
            self.account_type = 'admin'
        super().save(*args, **kwargs)

    class Meta:
        app_label='accounts'

class FranchiseDetails(models.Model):
    FRANCHISEE_TYPE_CHOICES = (
        ('MF', 'MF - Master Franchisee'),
        ('DF', 'DF - District Franchisee'),
        ('DCF', 'DCF - District City Franchisee')
    )

    PROGRAM_NAME_CHOICES = (
        ('abacus', 'Abacus'),
        ('vedic_maths', 'Vedic Maths'),
        ('handwriting', 'Handwriting'),
        ('calligraphy', 'Calligraphy'),
        ('robotic', 'Robotic')
    )

    BLOOD_GROUP_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )

    FIND_US_CHOICES = (
        ('existing_franchisee', 'Existing Franchisee'),
        ('google', 'Google'),
        ('other', 'Other')
    )

    photo = models.ImageField(upload_to='franchise_photos/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])], null=True, blank=True, max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    franchisee_type = models.CharField(max_length=3, choices=FRANCHISEE_TYPE_CHOICES)
    program_name = models.TextField(max_length=200, choices=PROGRAM_NAME_CHOICES, blank=True) 
    dob = models.DateField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    center_address = models.TextField()
    communication_address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    educational_qualification = models.CharField(max_length=100)
    present_occupation = models.CharField(max_length=100)
    annual_income = models.DecimalField(max_digits=10, decimal_places=2)
    experience_in_franchisee_model = models.PositiveIntegerField()
    find_about_us = models.CharField(max_length=20, choices=FIND_US_CHOICES)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,limit_choices_to={'account_type': 'franchisee'}, related_name='franchise_details')

    def set_program_name(self, program_list):
        self.program_name = ','.join(program_list)

    def get_program_name(self):
        return self.program_name.split(',')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.program_name} Franchisee"

    

class TeacherDetails(models.Model):
    PROGRAM_CHOICES = [
        ('abacus', 'Abacus'),
        ('vedic_maths', 'Vedic Maths'),
        ('handwriting', 'Handwriting'),
        ('calligraphy', 'Calligraphy'),
    ]

    SOURCE_CHOICES = [
        ('existing', 'Existing'),
        ('franchise', 'Franchise'),
        ('google', 'Google'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='teacher_photos/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])], null=True, blank=True, max_length=255)
    centre_name = models.CharField(max_length=255)
    franchise = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={'account_type': 'franchisee'}
    )
    program_name = models.CharField(max_length=20, choices=PROGRAM_CHOICES)
    dob = models.DateField()
    blood_group = models.CharField(max_length=5)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=15)
    email = models.EmailField()
    qualification = models.CharField(max_length=255)
    present_occupation = models.CharField(max_length=255)
    annual_income = models.DecimalField(max_digits=10, decimal_places=2)
    how_did_you_come_to_know_us = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    date = models.DateField(auto_now_add=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'account_type': 'teacher'}, related_name='teacher_details')


    def __str__(self):
        return f"{self.name} - {self.centre_name}"
    
class TeacherLevel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'account_type': 'teacher'}, related_name='teacher_level')
    prev_level = models.PositiveIntegerField(null=True)
    prev_level_date = models.DateField(null=True)
    due_date = models.DateField(null=True)

    def save(self, *args, **kwargs):
        # Calculate due_date based on prev_level_date
        if self.prev_level_date:
            self.due_date = self.prev_level_date + timedelta(days=2*30)  # assuming 30 days per month
        super().save(*args, **kwargs)
