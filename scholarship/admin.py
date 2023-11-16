from django.contrib import admin

from scholarship.models import (
    PersonalInformation,
    HighSchool,
    AcademicCounselor,
    CurrentEmployment,
    Parent,
    Household,
    TemporaryStorage,
    Attachments,
)

admin.site.register(PersonalInformation)
admin.site.register(HighSchool)
admin.site.register(AcademicCounselor)
admin.site.register(CurrentEmployment)
admin.site.register(Parent)
admin.site.register(Household)
admin.site.register(TemporaryStorage)
admin.site.register(Attachments)
