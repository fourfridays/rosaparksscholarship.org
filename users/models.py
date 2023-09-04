from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

    first_name = models.CharField(max_length=254, blank=False)
    last_name = models.CharField(max_length=254, blank=False)
    email = models.EmailField(_("email address"), unique=True, blank=False)
    is_staff = models.BooleanField(
        default=False,
        help_text=_(
            "Whether the user is a Staff member or not. "
            "Controls whether the user can log into this admin site."
        ),
    )
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = UserManager()

    def __str__(self):
        return self.email
