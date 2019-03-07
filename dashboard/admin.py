# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Status, Subscriptions, Lesson



class statusAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Status, statusAdmin)

class subscriptionsAdmin(admin.ModelAdmin):
    list_display = ('subscription_date','account', 'status')
admin.site.register(Subscriptions, subscriptionsAdmin)


class lessonAdmin(admin.ModelAdmin):
    list_display = ('date', 'description')
admin.site.register(Lesson, lessonAdmin)
