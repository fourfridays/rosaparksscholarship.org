from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_student",
        "is_judge",
        "is_staff",
    ]
    list_filter = (
        "is_active",
        "is_student",
        "is_judge",
        "is_staff",
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "phone_number", "dob")}),
        (
            "Address",
            {
                "fields":
                    (
                        "address1",
                        "address2",
                        "city",
                        "state",
                        "zip_code",
                    )
            }
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_student",
                    "is_judge",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(User, CustomUserAdmin)
