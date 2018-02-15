# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 10:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0033_auto_20171102_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_chat',
            name='chat_datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 2, 10, 48, 41, 67789, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='boarder',
            name='presence_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 2, 10, 48, 41, 67789, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='temp_chat',
            name='chat_datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 2, 10, 48, 41, 67789, tzinfo=utc)),
        ),
    ]
