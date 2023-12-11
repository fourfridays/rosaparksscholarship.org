from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin
from django.views.generic import TemplateView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap

from page.views import wagtail_admin_login
from scholarship.views import (
    ScholarshipAttachmentView,
    ScholarshipView,
    ScholarshipListView,
    ScholarshipDownloadExcelView,
    ScholarshipDeleteView,
)
from scholarship.forms import (
    PersonalInformationForm,
    HighSchoolForm,
    AcademicCounselorForm,
    CurrentEmploymentForm,
    ParentForm,
    HouseholdForm,
    CollegeForm,
    OtherForm,
)


urlpatterns = [
    re_path(
        r"^robots\.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    re_path(r"^sitemap\.xml$", sitemap),
    path(
        "scholarship/application/",
        ScholarshipView.as_view(
            [
                PersonalInformationForm,
                HighSchoolForm,
                AcademicCounselorForm,
                CurrentEmploymentForm,
                ParentForm,
                HouseholdForm,
                CollegeForm,
                OtherForm,
            ]
        ),
        name="scholarship-application",
    ),
    path("scholarship/application/closed/", TemplateView.as_view(template_name="scholarship/closed.html"), name="scholarship-application-closed"),
    path(
        "scholarship/application/list/", ScholarshipListView.as_view(), name="scholarship-application-list"
    ),
    path(
        "scholarship/application/delete/", ScholarshipDeleteView.as_view(),name="scholarship-application-delete"
    ),
    path(
        "scholarship/application/success/",
        TemplateView.as_view(template_name="scholarship/success.html"),
        name="scholarship-application-success",
    ),
    path(
        "scholarship/application/attachments/",
        ScholarshipAttachmentView.as_view(),
        name="scholarship-application-attachments",
    ),
    path("scholarship/application/download-excel/", ScholarshipDownloadExcelView.as_view(), name="scholarship-application-download-excel"),
    path("__debug__/", include("debug_toolbar.urls")),
    path("documents/", include(wagtaildocs_urls)),
    path("", include("allauth.urls")),
    # Override the Wagtail admin login URL
    path("admin/login/", wagtail_admin_login),
    path("django-admin/login/", wagtail_admin_login),
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
