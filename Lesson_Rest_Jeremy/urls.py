from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

from account.urls import url
from dashboard.urls import url

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"", include("rest_framework_docs.urls")),
    url(r"^api-auth", include("rest_framework.urls")),
    url(r"^account/", include("account.urls")),
    url(r"^dashboard/", include("dashboard.urls")),
]
