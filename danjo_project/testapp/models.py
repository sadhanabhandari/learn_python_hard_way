# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=50)
    marks = models.IntegerField()
