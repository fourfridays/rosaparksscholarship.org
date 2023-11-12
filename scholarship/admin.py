from django.contrib import admin

from scholarship.models import (
    PersonalInformation,
    StudentEmploymentHistory,
    Parent1,
    Parent2,
    Household,
    TemporaryStorage
)

admin.site.register(PersonalInformation)
admin.site.register(StudentEmploymentHistory)
admin.site.register(Parent1)
admin.site.register(Parent2)
admin.site.register(Household)
admin.site.register(TemporaryStorage)
