# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, CreateAPIView
from rest_framework.views import APIView
from dashboard.models import Status, Subscriptions, Lesson
from dashboard.serializers import LessonSerializer, LessonEnrollSerializer, LessonStudentSerializer, \
    SubscriptionsLessonSerializer, SubscriptionsSerializer, SubscriptionsStatusSerializer

class SubscriptionsCreateList(ListCreateAPIView):
    ''' Generic List and create for Subscriptions '''
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer

class LessonCreateList(ListCreateAPIView):
    ''' Generic List and create view for lessons'''
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonList(ListAPIView):
    ''' Generic List view for lessons with overide query_set in order render full list 
    or single lesson if one id is given'''
    serializer_class = LessonStudentSerializer

    def get_queryset(self):
        id = self.kwargs['id']

        return Lesson.objects.filter(lesson_id=id) if id else Lesson.objects.all()

class EnrollStudentLesson(CreateAPIView):
    ''' Generic Create view to enroll a student to a lesson '''
    serializer_class = LessonEnrollSerializer


class UpdateStatusSubscription(ListCreateAPIView):
    ''' Generic List and create view to update the subscription status and using an overide create methode
     to update a status using the subscription id as kwargs'''
    queryset = Subscriptions.objects.all()
    serializer_class= SubscriptionsStatusSerializer


    def create(self, request, *args, **kwargs):
        
        subscriptions = Subscriptions.objects.get(subscription_id=request.data['subscription_id']) #get subscription_id instance in order to update
        serializer = self.get_serializer(subscriptions, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SubscriptionsList(ListAPIView):
    ''' Generic List view to render all subscriptions with an overide queryset in order to list all subscriptions 
    or a selected one using the id as kwargs'''
    serializer_class = SubscriptionsLessonSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        
        return Subscriptions.objects.filter(subscription_id=id) if id else Subscriptions.objects.all()