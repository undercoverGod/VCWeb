# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0068_auto_20180105_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storekeeper',
            name='Store_Half',
            field=models.CharField(choices=[('MOn', 'Morning'), ('EVn', 'Evening')], max_length=12, unique_for_date='Store_Date'),
        ),
    ]
