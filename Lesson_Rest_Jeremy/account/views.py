# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, ListCreateAPIView
from account.models import Account, Students
from account.serializers import StudentsAccountSerializer, AccountStudentSerializer, StudentsSerializer, AccountSerializer


class AccountList(ListAPIView):
    serializer_class = AccountStudentSerializer

    def get_queryset(self):
        """
        This view should return either a list of all account if no id is given or the information of the selected account.
        """
        id = self.kwargs['id']
        if id:

            return Account.objects.filter(account_id=id)
        else:
            return Account.objects.all()


class AccountCreateList(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer



class StudentsCreateList(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsAccountSerializer
