from django.conf.urls import url
from django.contrib import admin

from rest_framework.generics import RetrieveAPIView

from dashboard.models import Lesson, Status, Subscriptions
from account.models import Account
from dashboard.serializers import (
    LessonEnrollSerializer,
    LessonSerializer,
    SubscriptionsLessonSerializer,
    SubscriptionsSerializer,
    AccountSubscriptionsListSerializer,
)
from dashboard.views import (
    StatusList,
    EnrollStudentLesson,
    LessonCreateList,
    LockLesson,
    LessonList,
    SubscriptionsCreateList,
    SubscriptionsList,
    UpdateStatusSubscription,
    SubscriptionsAccountList,
)

app_name = "dashboard"

urlpatterns = [
    url(r"^create_sub$", SubscriptionsCreateList.as_view(), name="dash_create_sub"),
    url(r"^all_status$", StatusList.as_view(), name="dash_status"),
    url(
        r"^subscriptions/(?:(?P<id>\d+)/)?$",
        SubscriptionsAccountList.as_view(
            queryset=Account.objects.all(),
            serializer_class=AccountSubscriptionsListSerializer,
        ),
        name="dash_sub_account",
    ),
    url(
        r"^update_status", UpdateStatusSubscription.as_view(), name="dash_update_status"
    ),
    url(r"^create_lesson$", LessonCreateList.as_view(), name="dash_create_lesson"),
    url(r"^lesson/(?:(?P<id>[0-9]+)/)?$", LessonList.as_view(), name="dash_lesson"),
    url(r"^enrol_student$", EnrollStudentLesson.as_view(), name="dash_enrol_student"),
    url(
        r"^subscription_lessons/(?:(?P<id>[0-9]+)/)?$",
        SubscriptionsList.as_view(),
        name="dash_sub_lessons",
    ),
    url(
        r"^lock_lesson/(?:(?P<pk>[0-9]+)/)?$", LockLesson.as_view(), name="lock_lesson"
    ),
]
