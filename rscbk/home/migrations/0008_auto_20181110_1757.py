# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-10 17:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_userfullprofile_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfullprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userdetails', to=settings.AUTH_USER_MODEL),
        ),
    ]