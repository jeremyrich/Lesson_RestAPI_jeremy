# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Account(models.Model): 

    account_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=False)
    email = models.EmailField(unique=True, max_length=45, null=False)
    password = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=200, null=False)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Students(models.Model):

    students_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45, null=False)
    last_name = models.CharField(max_length=45, null=False)
    birthday = models.DateField()
    email = models.EmailField(unique=True, max_length=45, null=False)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    account = models.ForeignKey(Account, related_name='students', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Students"

    def __str__(self):
        return self.first_name