# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-07 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                ("account_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=45)),
                ("email", models.EmailField(max_length=45, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=200)),
                ("insert_date", models.DateTimeField(auto_now_add=True)),
                ("update_date", models.DateTimeField(auto_now=True)),
            ],
        )
    ]
