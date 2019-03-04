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

from dashboard.serializers import LessonSerializer, SubscriptionsStatusSerializer, SubscriptionsLessonSerializer, SubscriptionsSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView
from dashboard.models import Status, Subscriptions, Lesson
from account.models import Account, Students
import dashboard.views as views

app_name = 'dashboard'

urlpatterns = [
    url(r'^create_sub$', ListCreateAPIView.as_view(queryset=Subscriptions.objects.all(), 
    serializer_class=SubscriptionsSerializer), name='dash_create_sub'),
    url(r'^update_status$', UpdateAPIView.as_view(queryset=Subscriptions.objects.all(), 
    serializer_class=SubscriptionsSerializer), name='dash_update_status'),
]

