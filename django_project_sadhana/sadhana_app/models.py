# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    description = models.CharField(max_length=50)

