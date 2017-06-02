# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
