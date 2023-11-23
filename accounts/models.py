from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ACCOUNT_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('franchisee', 'Franchisee'),
        ('teacher', 'Teacher')
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

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    franchisee_type = models.CharField(max_length=3, choices=FRANCHISEE_TYPE_CHOICES)
    program_name = models.CharField(max_length=20, choices=PROGRAM_NAME_CHOICES)
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
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='franchise_details')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.program_name} Franchisee"

    
