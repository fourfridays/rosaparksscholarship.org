from django.contrib import admin

from scholarship.models import (
    PersonalInformation,
    HighSchool,
    AcademicCounselor,
    CurrentEmployment,
    Parent,
    Household,
    College,
    Other,
    TemporaryStorage,
    Attachments,
)

admin.site.register(PersonalInformation)
admin.site.register(HighSchool)
admin.site.register(AcademicCounselor)
admin.site.register(CurrentEmployment)
admin.site.register(Parent)
admin.site.register(Household)
admin.site.register(College)
admin.site.register(Other)
admin.site.register(TemporaryStorage)
admin.site.register(Attachments)
