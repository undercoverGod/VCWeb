# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-06 01:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boarder',
            name='Evening_Presence',
        ),
        migrations.RemoveField(
            model_name='boarder',
            name='Morning_Presence',
        ),
        migrations.RemoveField(
            model_name='boarder',
            name='Presence_Date',
        ),
    ]
