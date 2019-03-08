from django.conf.urls import url, include
from django.contrib import admin
from account.urls import url
from dashboard.urls import url
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('rest_framework_docs.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^dashboard/', include('dashboard.urls')),

]
