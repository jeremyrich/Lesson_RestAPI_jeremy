# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def home(request):

    return HttpResponse('Welcome to account Homepage!')