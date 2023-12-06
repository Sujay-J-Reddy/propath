from django.contrib import admin
from .models import Birthdays, LevelCertificates, Competition, CompetitionRegister

# Register your models here.
admin.site.register(LevelCertificates)
admin.site.register(Birthdays)
admin.site.register(Competition)
admin.site.register(CompetitionRegister)
