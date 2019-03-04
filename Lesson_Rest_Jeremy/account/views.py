# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from rest_framework.generics import ListAPIView, ListCreateAPIView
from account.models import Account, Students
from account.serializers import AccountStudentSerializer, StudentsSerializer, AccountSerializer

class AccountList(ListAPIView):
    serializer_class = AccountStudentSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        id = self.kwargs['id']
        if id:

            return Account.objects.filter(account_id=id)
        else:
            return Account.objects.all()