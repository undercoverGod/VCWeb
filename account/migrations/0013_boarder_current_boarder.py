# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-13 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20180225_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='boarder',
            name='Current_Boarder',
            field=models.BooleanField(default=True),
        ),
    ]