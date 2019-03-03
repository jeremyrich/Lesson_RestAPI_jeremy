# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Account, Students


class accountAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'address')

admin.site.register(Account, accountAdmin)


class studentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'birthday', 'email')

admin.site.register(Students, studentAdmin)
