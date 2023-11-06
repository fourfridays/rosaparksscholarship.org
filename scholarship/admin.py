from django.contrib import admin

from scholarship.models import (
    PersonalInformation,
    EmploymentHistory,
    Parent1,
    Parent2,
    Household,
    TemporaryStorage
)

admin.site.register(PersonalInformation)
admin.site.register(EmploymentHistory)
admin.site.register(Parent1)
admin.site.register(Parent2)
admin.site.register(Household)
admin.site.register(TemporaryStorage)
