from django.contrib import admin

from scholarship.models import (
    PersonalInformation,
    StudentEmploymentHistory,
    Parent,
    Household,
    TemporaryStorage
)

admin.site.register(PersonalInformation)
admin.site.register(StudentEmploymentHistory)
admin.site.register(Parent)
admin.site.register(Household)
admin.site.register(TemporaryStorage)
