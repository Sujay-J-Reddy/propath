# admin.py

from django.contrib import admin
from .models import CustomUser, FranchiseDetails

admin.site.register(CustomUser)
admin.site.register(FranchiseDetails)

