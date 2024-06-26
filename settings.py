import logging
import os
import dj_database_url

from distutils.util import strtobool
from pathlib import Path
from wagtail.embeds.oembed_providers import youtube


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Doing this boolean check against str values. Can't set boolean values in configmap
DEBUG = os.environ.get("DJANGO_DEBUG") == "True"

INSTALLED_APPS = [
    "anymail",
    "article",
    "crispy_forms",
    "crispy_bootstrap5",
    "formtools",
    "page",
    "phonenumber_field",
    "scholarship",
    "sponsor",
    "users",
    "wagtailcodeblock",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.styleguide",
    "wagtail.contrib.table_block",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sitemaps",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # django-allauth
    "django.contrib.sites",
    "allauth",
    "allauth.account",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

sentry_dsn = os.environ.get("SENTRY_DSN", "")
if sentry_dsn:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration
    from sentry_sdk.integrations.logging import LoggingIntegration
    
    # The SDK will honor the level set by the logging library, which is WARNING by default.
    # If we want to capture records with lower severity, we need to configure
    # the logger level first.
    logging.basicConfig(level=logging.INFO)

    def ignore_disallowedhost(event, hint):
        if event.get("logger", None) == "django.security.DisallowedHost":
            return None
        return event

    sentry_sdk.init(
        dsn=sentry_dsn,
        before_send=ignore_disallowedhost,
        integrations=[
            LoggingIntegration(
                level=logging.INFO,        # Capture info and above as breadcrumbs
                event_level=logging.INFO   # Send records as events
            ),
            DjangoIntegration(),
        ],
        traces_sample_rate=0.2,
        send_default_pii=True,
    )

ROOT_URLCONF = "urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "wsgi.application"

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite://:memory:")
DATABASES = {"default": dj_database_url.parse(DATABASE_URL)}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 8,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

# SESSION DB
SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 1209600  # Two weeks, in seconds

# Required for django.contrib.sites for django-allauth
SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = ["static"]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

staticfiles_backend = "django.contrib.staticfiles.storage.StaticFilesStorage"
STATIC_URL = "/static/"

if DEBUG is True:
    storage_backend = "django.core.files.storage.FileSystemStorage"
    MEDIA_URL = "media/"
    MEDIA_ROOT = os.path.join("/data/media")
else:
    AWS_S3_ACCESS_KEY_ID = os.environ.get("AWS_S3_ACCESS_KEY_ID", default=None)
    AWS_S3_SECRET_ACCESS_KEY = os.environ.get("AWS_S3_SECRET_ACCESS_KEY", default=None)
    AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", default=None)
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = "d2s34nehzymfnm.cloudfront.net"
    AWS_IS_GZIPPED = os.environ.get("AWS_IS_GZIPPED", default=True)
    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000",
    }
    # S3 static settings
    # STATIC_LOCATION = "static"
    # STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/"
    # staticfiles_backend = "page.storage_backends.StaticStorage"
    # S3 public media settings
    PUBLIC_MEDIA_LOCATION = "media"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/"
    storage_backend = "page.storage_backends.PublicMediaStorage"
    # S3 private media settings
    PRIVATE_MEDIA_LOCATION = "private"
    PRIVATE_FILE_STORAGE = "page.storage_backends.PrivateMediaStorage"

STORAGES = {
    "default": {"BACKEND": storage_backend},
    "staticfiles": {"BACKEND": staticfiles_backend},
}

# Wagtail settings
WAGTAIL_SITE_NAME = os.environ.get(
    "WAGTAIL_SITE_NAME", default="Rosa Parks Scholarship Foundation"
)

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = os.environ.get("WAGTAILADMIN_BASE_URL", default="localhost")

DOMAIN_ALIASES = [
    d.strip() for d in os.environ.get("DOMAIN_ALIASES", "").split(",") if d.strip()
]
ALLOWED_HOSTS = DOMAIN_ALIASES
CSRF_TRUSTED_ORIGINS = [
    os.environ.get("CSRF_TRUSTED_ORIGINS", default="http://localhost")
]
SECRET_KEY = os.environ.get("SECRET_KEY", default="<a string of random characters>")

# Custom User model
AUTH_USER_MODEL = "users.User"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Make low-quality but small images
WAGTAILIMAGES_AVIF_QUALITY = 60
WAGTAILIMAGES_JPEG_QUALITY = 60
WAGTAILIMAGES_WEBP_QUALITY = 65
WAGTAIL_ENABLE_WHATS_NEW_BANNER = False
WAGTAILEMBEDS_FINDERS = [
    # Fetches YouTube videos but puts ``?scheme=https`` in the GET parameters
    # when calling YouTube's oEmbed endpoint
    {
        "class": "wagtail.embeds.finders.oembed",
        "providers": [youtube],
        "options": {"scheme": "https"},
    },
    # Handles all other oEmbed providers the default way
    {
        "class": "wagtail.embeds.finders.oembed",
    },
]
WAGTAILEMBEDS_RESPONSIVE_HTML = True

# wagtailcodeblock
WAGTAIL_CODE_BLOCK_LINE_NUMBERS = False
WAGTAIL_CODE_BLOCK_THEME = "tomorrow"

WAGTAILIMAGES_FORMAT_CONVERSIONS = {
    "avif": "avif",
    "bmp": "jpeg",
    "webp": "webp",
}

WAGTAIL_PAGES_IS_CREATABLE = os.environ.get("WAGTAIL_PAGES_IS_CREATABLE", False)

# DJANGO ANYMAIL
ANYMAIL = {
    "MAILGUN_API_KEY": os.getenv("MAILGUN_API_KEY", default=""),
    "MAILGUN_SENDER_DOMAIN": os.getenv("MAILGUN_SENDER_DOMAIN", default=""),
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", default="")
SERVER_EMAIL = os.getenv("SERVER_EMAIL", default="")

# ALLAUTH
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_CONFIRMATION_HMAC = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_MAX_EMAIL_ADDRESSES = 1
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_FORMS = {
    "signup": "users.forms.CustomSignupForm",
}

# GOOGLE RECAPTCHA
# RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_PUBLIC_KEY", default="")
# RECAPTCHA_PRIVATE_KEY = os.getenv("RECAPTCHA_PRIVATE_KEY", default="")

# CRISPY FORMS
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


# DJANGO DEBUG TOOLBAR
def show_toolbar(request=None):
    return bool(strtobool(os.environ.get("DJANGO_DEBUG", "True")))


if show_toolbar():
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": show_toolbar,
        "SHOW_COLLAPSED": True,
    }
