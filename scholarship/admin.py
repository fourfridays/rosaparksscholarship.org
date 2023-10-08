from django.contrib import admin

from scholarship.models import PersonalInformation, EmploymentHistory, FamilyInformation

admin.site.register(PersonalInformation)
admin.site.register(EmploymentHistory)
admin.site.register(FamilyInformation)
