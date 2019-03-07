"""Lesson_Rest_Jeremy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from dashboard.serializers import LessonSerializer, LessonEnrollSerializer, SubscriptionsLessonSerializer, SubscriptionsSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView
from dashboard.models import Status, Subscriptions, Lesson
from dashboard.views import SubscriptionsCreateList, LessonCreateList, LessonList, enrollStudentLesson, SubscriptionsList, updateStatusSubscription

app_name = 'dashboard'

urlpatterns = [
    url(r'^create_sub$', SubscriptionsCreateList.as_view(), name='dash_create_sub'),
    url(r'^update_status', updateStatusSubscription.as_view(), name='dash_update_status'),
    # url(r'^update_status/(?:(?P<pk>\d+)/)?$', updateStatusSubscription.as_view(), name='dash_update_status'),
    url(r'^create_lesson$', LessonCreateList.as_view(), name='dash_create_lesson'),
    url(r'^lesson/(?:(?P<id>[0-9]+)/)?$', LessonList.as_view(), name='dash_lesson'),
    url(r'^enrol_student$', enrollStudentLesson.as_view(), name='dash_enrol_student'),
    url(r'^subscription/(?:(?P<id>[0-9]+)/)?$', SubscriptionsList.as_view(), name='dash_sub'),

]

