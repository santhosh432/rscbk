# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
class Brand(models.Model):
    DEFAULT_PK=1
    brand_name = models.CharField(max_length=15, help_text='brand name')

    def __str__(self):
        return '{0}'.format(self.brand_name)


# Create your models here.

def mobilevalid(value):
    if len(value) != 10:
        raise ValidationError('10 digit required')

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    mobile = models.CharField(max_length=10, help_text='10 digit mobile number')
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=10, blank=True, null=True)


class UserFullProfile(models.Model):
    user = models.OneToOneField(User , related_name='userdetails')
    mobile = models.CharField(max_length=10, help_text='10 digit mobile number')
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=10, blank=True, null=True)
    user_image = models.ImageField(upload_to='user_image/', help_text='Upload user image',default='null')




class Feedback(models.Model):
    customer_name = models.CharField(max_length=120)
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_name

