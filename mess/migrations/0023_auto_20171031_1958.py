# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 14:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0022_auto_20171031_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='chat',
            name='chat_datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 31, 19, 58, 8, 624697)),
        ),
    ]