from django.conf.urls import url
from django.contrib import admin

from account.serializers import AccountStudentSerializer, StudentsSerializer, AccountSerializer
from account.models import Account, Students
from account.views import AccountList, AccountCreateList, StudentsCreateList

app_name = 'account'

urlpatterns = [
    url(r'^(?:(?P<id>[0-9]+)/)?$', AccountList.as_view(), name='account_get'),
    url(r'^create$', AccountCreateList.as_view(), name='account_create'),
    url(r'^create_student$', StudentsCreateList.as_view(), name='account_create_student'),
]

