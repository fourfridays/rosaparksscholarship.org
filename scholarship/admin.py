from django.contrib import admin

from scholarship.models import (
    PersonalInformation,
    HighSchool,
    AcademicCounselor,
    HonorOrAward,
    ExtraCurricular,
    CurrentEmployment,
    Parent,
    Household,
    TemporaryStorage
)

admin.site.register(PersonalInformation)
admin.site.register(HighSchool)
admin.site.register(AcademicCounselor)
admin.site.register(HonorOrAward)
admin.site.register(ExtraCurricular)
admin.site.register(CurrentEmployment)
admin.site.register(Parent)
admin.site.register(Household)
admin.site.register(TemporaryStorage)
