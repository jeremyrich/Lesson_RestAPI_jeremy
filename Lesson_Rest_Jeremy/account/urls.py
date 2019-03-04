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

from account.serializers import AccountStudentSerializer, StudentsSerializer, AccountSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView
from account.models import Account, Students
from account.views import AccountList

app_name = 'account'

urlpatterns = [
    url(r'^(?:(?P<id>[0-9]+)/)?$', AccountList.as_view(), name='account'),
    url(r'^create$', ListCreateAPIView.as_view(queryset=Account.objects.all(), 
    serializer_class=AccountSerializer), name='account_create'),
    url(r'^create_student$', ListCreateAPIView.as_view(queryset=Students.objects.all(), 
    serializer_class=StudentsSerializer), name='account_create_student'),
]

