# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Brand,UserFullProfile,Feedback


@admin.register(UserFullProfile)
class UserFullProfileAdmin(admin.ModelAdmin):
   pass

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand_name']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass