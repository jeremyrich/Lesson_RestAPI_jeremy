
from django.conf.urls import url
from django.contrib import admin

from dashboard.serializers import LessonSerializer, LessonEnrollSerializer, SubscriptionsLessonSerializer, \
    SubscriptionsSerializer
from dashboard.models import Status, Subscriptions, Lesson
from dashboard.views import SubscriptionsCreateList, LessonCreateList, LessonList, EnrollStudentLesson, \
    SubscriptionsList, UpdateStatusSubscription

app_name = 'dashboard'

urlpatterns = [
    url(r'^create_sub$', SubscriptionsCreateList.as_view(), name='dash_create_sub'),
    url(r'^update_status', UpdateStatusSubscription.as_view(), name='dash_update_status'),
    url(r'^create_lesson$', LessonCreateList.as_view(), name='dash_create_lesson'),
    url(r'^lesson/(?:(?P<id>[0-9]+)/)?$', LessonList.as_view(), name='dash_lesson'),
    url(r'^enrol_student$', EnrollStudentLesson.as_view(), name='dash_enrol_student'),
    url(r'^subscription/(?:(?P<id>[0-9]+)/)?$', SubscriptionsList.as_view(), name='dash_sub'),

]

