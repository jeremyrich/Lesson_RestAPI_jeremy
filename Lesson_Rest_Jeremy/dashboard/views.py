# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, ListCreateAPIView
from dashboard.models import Status, Subscriptions, Lesson
from dashboard.serializers import LessonSerializer, LessonStudentSerializer, SubscriptionsStatusSerializer, SubscriptionsLessonSerializer, SubscriptionsSerializer

class SubscriptionsCreateList(ListCreateAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer

class LessonCreateList(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonList(ListAPIView):
    serializer_class = LessonStudentSerializer

    def get_queryset(self):
        """
        This view should return either a list of all account if no id is given or the information of the selected account.
        """
        id = self.kwargs['id']
        if id:

            return Lesson.objects.filter(account_id=id)
        else:
            return Lesson.objects.all()