# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0046_auto_20171110_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boarder',
            name='Evening_Presence',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='boarder',
            name='Morning_Presence',
            field=models.BooleanField(default=False),
        ),
    ]
