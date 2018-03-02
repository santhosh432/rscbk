# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-02 04:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(help_text='item short description', max_length=25)),
                ('item_full_desc', models.CharField(help_text='item full description', max_length=200)),
                ('price', models.PositiveIntegerField(help_text='Item price')),
                ('location', models.CharField(help_text='Item location', max_length=50)),
                ('months_used', models.PositiveSmallIntegerField(help_text='No of Years')),
                ('years_used', models.PositiveSmallIntegerField(help_text='No of Months')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
            ],
        ),
    ]