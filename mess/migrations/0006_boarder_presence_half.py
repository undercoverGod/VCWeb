# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0005_auto_20171027_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='boarder',
            name='presence_half',
            field=models.CharField(choices=[('MO', 'Morning'), ('EV', 'Evening')], default='MO', max_length=12, unique_for_date='meal_date'),
        ),
    ]
