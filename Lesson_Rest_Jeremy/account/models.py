# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Account(models.Model): 
    """

    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, null=True)
    email = models.EmailField(max_length=45, null=True)
    password = models.CharField(max_length=45, null=True)
    address = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


