# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-08 13:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20190308_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='students',
            new_name='students_id',
        ),
    ]
