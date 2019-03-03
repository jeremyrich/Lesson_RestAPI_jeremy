# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from account.serializers import AccountSerializer, StudentsSerializer
from rest_framework import generics
from account.models import Account, Students

