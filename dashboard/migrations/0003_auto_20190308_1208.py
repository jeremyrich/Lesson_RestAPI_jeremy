# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-08 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20190308_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='subscription_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]