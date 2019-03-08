# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from account.models import Account, Students

class Status(models.Model):

    status_id = models.AutoField(primary_key=True)

    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Paused', 'Paused'),
        ('Cancelled', 'Cancelled'),
    )

    name = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES,
        default='ACTIVE',
        null=False
    )

    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Status"

    def __str__(self):
        return self.name


class Subscriptions(models.Model): 

    subscription_id = models.AutoField(primary_key=True)
    subscription_date = models.DateField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    account_id = models.ForeignKey(Account, related_name='subscriptions', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, related_name='subscriptions', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return str(self.subscription_id)

    class Meta:
        verbose_name_plural = "Subscriptions"

class Lesson(models.Model):

    lesson_id = models.AutoField(primary_key=True)
    date = models.DateField()
    description = models.TextField(null=False)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    subscription_id = models.ForeignKey(Subscriptions, related_name='lessons', on_delete=models.SET_NULL, null=True)
    student_id = models.ManyToManyField(Students)

    def __str__(self):
        return self.description





