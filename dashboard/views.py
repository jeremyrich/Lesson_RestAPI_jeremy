# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView
from dashboard.models import Status, Subscriptions, Lesson
from dashboard.serializers import LessonSerializer, LessonEnrollSerializer, LessonStudentSerializer, SubscriptionsLessonSerializer, SubscriptionsSerializer, SubscriptionsStatusSerializer

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

class enrollStudentLesson(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonEnrollSerializer
        

class updateStatusSubscription(ListCreateAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class= SubscriptionsStatusSerializer

    def create(self, request, *args, **kwargs):
        
        subscriptions = Subscriptions.objects.get(subscription_id=request.data['subscription_id'])
        serializer = self.get_serializer(subscriptions, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SubscriptionsList(ListAPIView):
    serializer_class = SubscriptionsLessonSerializer

    def get_queryset(self):
        """
        This view should return either a list of all account if no id is given or the information of the selected account.
        """
        id = self.kwargs['id']
        if id:

            return Subscriptions.objects.filter(subscription_id=id)
        else:
            return Subscriptions.objects.all()