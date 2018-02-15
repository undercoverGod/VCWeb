# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0038_futureboarder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='futureboarder',
            name='offhalf',
            field=models.CharField(choices=[('MO', 'Morning'), ('EV', 'Evening')], max_length=12, unique_for_date='offdate'),
        ),
        migrations.AlterField(
            model_name='futureboarder',
            name='onhalf',
            field=models.CharField(choices=[('MO', 'Morning'), ('EV', 'Evening')], max_length=12, unique_for_date='ondate'),
        ),
    ]