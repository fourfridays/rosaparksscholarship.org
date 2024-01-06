from django.urls import reverse

from wagtail import hooks
from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup

from scholarship.models import (
    PersonalInformation,
    HighSchool,
    AcademicCounselor,
    CurrentEmployment,
    Parent,
    Household,
    College,
    Other,
)


class PersonalInformationViewSet(SnippetViewSet):
    model = PersonalInformation
    list_display = ["user"]
    ordering = ["user__email"]
    search_fields = ["user__email"]

    panels = [
        FieldPanel("address1"),
        FieldPanel("address2"),
        FieldPanel("city"),
        FieldPanel("state"),
        FieldPanel("zip_code"),
        FieldPanel("phone_number"),
        FieldPanel("dob"),
        FieldPanel("place_of_birth"),
    ]


class HighSchoolViewSet(SnippetViewSet):
    model = HighSchool
    list_display = ["user"]
    ordering = ["user__email"]
    search_fields = ["user__email"]

    panels = [
        FieldPanel("name"),
        FieldPanel("city"),
        FieldPanel("graduation_date"),
        FieldPanel("gpa"),
    ]


class AcademicCounselorViewSet(SnippetViewSet):
    model = AcademicCounselor
    list_display = ["user"]
    ordering = ["user__email"]
    search_fields = ["user__email"]

    panels = [
        FieldPanel("name"),
        FieldPanel("phone_number"),
        FieldPanel("email"),
    ]


class CurrentEmploymentViewSet(SnippetViewSet):
    model = CurrentEmployment
    list_display = ["user"]
    ordering = ["user__email"]
    search_fields = ["user__email"]

    panels = [
        FieldPanel("employer_name"),
        FieldPanel("job_title"),
        FieldPanel("hours_per_week"),
    ]


class ParentViewSet(SnippetViewSet):
    model = Parent
    list_display = ["user"]
    ordering = ["user__email"]
    search_fields = ["user__email"]

    panels = [
        FieldPanel("parent_1_full_name"),
        FieldPanel("parent_1_email"),
        FieldPanel("parent_1_address1"),
        FieldPanel("parent_1_address2"),
        FieldPanel("parent_1_city"),
        FieldPanel("parent_1_state"),
        FieldPanel("parent_1_zip_code"),
        FieldPanel("parent_1_phone_number"),
        FieldPanel("parent_1_place_of_employment"),
        FieldPanel("parent_1_job_title"),
        FieldPanel("parent_2_full_name"),
        FieldPanel("parent_2_email"),
        FieldPanel("parent_2_address1"),
        FieldPanel("parent_2_address2"),
        FieldPanel("parent_2_city"),
        FieldPanel("parent_2_state"),
        FieldPanel("parent_2_zip_code"),
        FieldPanel("parent_2_phone_number"),
        FieldPanel("parent_2_place_of_employment"),
        FieldPanel("parent_2_job_title"),
    ]


class HouseholdViewSet(SnippetViewSet):
    model = Household
    list_display = ["user"]
    ordering = ["user__email"]
    search_fields = ["user__email"]

    panels = [
        FieldPanel("total_household_income"),
        FieldPanel("siblings_under_18"),
        FieldPanel("siblings_over_18"),
    ]


class CollegeViewSet(SnippetViewSet):
    model = College
    list_display = ["user"]
    ordering = ["user__email"]
    search_fields = ["user__email"]

    panels = [
        FieldPanel("goal"),
        FieldPanel("major"),
        FieldPanel("career"),
        FieldPanel("applied_for_1"),
        FieldPanel("applied_for_2"),
        FieldPanel("applied_for_3"),
        FieldPanel("plan_to_attend"),
        FieldPanel("savings"),
        FieldPanel("savings_by_guardian"),
        FieldPanel("financial_need"),
    ]


class OtherViewSet(SnippetViewSet):
    model = Other
    list_display = ["user"]
    ordering = ["user__email"]
    search_fields = ["user__email"]

    panels = [
        FieldPanel("foster_care"),
        FieldPanel("challenges"),
        FieldPanel("other_scholarships"),
        FieldPanel("other_scholarships_awarded"),
        FieldPanel("plan_to_pay"),
    ]


class ScholarshipViewSetGroup(SnippetViewSetGroup):
    items = (
        PersonalInformationViewSet,
        HighSchoolViewSet,
        AcademicCounselorViewSet,
        CurrentEmploymentViewSet,
        ParentViewSet,
        HouseholdViewSet,
        CollegeViewSet,
        OtherViewSet,
    )
    menu_icon = "folder-inverse"
    menu_label = "Scholarship Apps"
    menu_name = "scholarship-apps"


register_snippet(ScholarshipViewSetGroup)


@hooks.register("register_admin_menu_item")
def register_scholarship_menu_item():
    submenu = Menu(
        items=[
            MenuItem(
                "List",
                reverse("scholarship-application-list"),
                icon_name="link-external",
            ),
            MenuItem(
                "Delete",
                reverse("scholarship-application-delete"),
                icon_name="link-external",
            ),
        ]
    )

    return SubmenuMenuItem("Scholarship Admin", submenu, icon_name="folder-inverse")
