# admin.py

from django.contrib import admin
from .models import CustomUser, FranchiseDetails, TeacherDetails, TeacherLevel

admin.site.register(CustomUser)
admin.site.register(FranchiseDetails)
admin.site.register(TeacherDetails)
admin.site.register(TeacherLevel)

