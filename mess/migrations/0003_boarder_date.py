# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 20:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0002_auto_20171027_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='boarder',
            name='date',
            field=models.DateField(default=datetime.date(2017, 10, 27)),
        ),
    ]