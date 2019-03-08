# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, ListCreateAPIView
from account.models import Account, Students
from account.serializers import StudentsAccountSerializer, AccountStudentSerializer, StudentsSerializer, AccountSerializer


class AccountList(ListAPIView):
    ''' Generic List view for Accounts with overide query_set in order render full list 
    or single account if one id is given'''
    serializer_class = AccountStudentSerializer

    def get_queryset(self):
        id = self.kwargs['id']

        return Account.objects.filter(account_id=id) if id else Account.objects.all()
            


class AccountCreateList(ListCreateAPIView):
    ''' Generic List and create view for Accounts '''
    queryset = Account.objects.all()
    serializer_class = AccountSerializer



class StudentsCreateList(ListCreateAPIView):
    ''' Generic List and create view for Students '''
    queryset = Students.objects.all()
    serializer_class = StudentsAccountSerializer
