# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-27 10:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0017_catbrand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wishlist_name', models.CharField(help_text='item short description', max_length=25)),
                ('wishlist_full_desc', models.CharField(help_text='item full description', max_length=200)),
                ('wishlist_other_info', models.CharField(default='null', help_text='Item other information', max_length=150)),
                ('wishlist_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
                ('wishlist_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]