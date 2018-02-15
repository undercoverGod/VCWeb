# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 23:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0026_auto_20171101_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_chat',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='temp_chat',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='all_chat',
            name='chat_datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 5, 28, 37, 438468)),
        ),
        migrations.AlterField(
            model_name='temp_chat',
            name='chat_datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 5, 28, 37, 439466)),
        ),
    ]
