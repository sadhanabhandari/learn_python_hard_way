# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 00:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='marks',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='name',
        ),
    ]
