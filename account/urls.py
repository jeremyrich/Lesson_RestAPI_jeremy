from django.conf.urls import url
from django.contrib import admin

from account.models import Account, Students
from account.serializers import (
    AccountSerializer,
    AccountStudentSerializer,
    StudentsSerializer,
)
from account.views import (
    AccountCreateList,
    AccountList,
    StudentsCreateList,
    StudentsDeleteList,
)

app_name = "account"

urlpatterns = [
    url(r"^(?:(?P<id>[0-9]+)/)?$", AccountList.as_view(), name="account_get"),
    url(r"^create$", AccountCreateList.as_view(), name="account_create"),
    url(
        r"^create_student$", StudentsCreateList.as_view(), name="account_create_student"
    ),
    url(
        r"^delete_student/(?:(?P<pk>[0-9]+)/)?$",
        StudentsDeleteList.as_view(),
        name="account_delete_student",
    ),
]
